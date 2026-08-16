#!/usr/bin/env python3
"""Reproduce AF v6.2 Stage B structural-yield reference calculations.

The script fixes the RNG implementation, seed, ordinal cut points, latent
correlation construction, and dominance rule. Results quantify Monte Carlo
error under this model only; they are not forecasts about real candidates.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np

N_DIMS = 12
DEFAULT_DRAWS = 500_000
DEFAULT_SEED = 20260725
# Standard-normal quintile boundaries: Phi^-1(0.2, 0.4, 0.6, 0.8).
QUINTILE_CUTS = np.array(
    [-0.8416212335729143, -0.2533471031357997,
      0.2533471031357997,  0.8416212335729143],
    dtype=float,
)


def exact_k_category_dominance(k: int, n: int) -> float:
    return 2.0 * (((k + 1) / (2 * k)) ** n - (1 / k) ** n)


def exact_mixed_dominance(binary_dims: int, five_category_dims: int) -> float:
    return 2.0 * (
        (3 / 4) ** binary_dims * (3 / 5) ** five_category_dims
        - (1 / 2) ** binary_dims * (1 / 5) ** five_category_dims
    )


def correlated_profile(
    rng: np.random.Generator, draws: int, dimensions: int, rho: float
) -> np.ndarray:
    common = rng.standard_normal((draws, 1))
    residual = rng.standard_normal((draws, dimensions))
    latent = math.sqrt(rho) * common + math.sqrt(1 - rho) * residual
    return np.digitize(latent, QUINTILE_CUTS)


def simulate(rho: float, draws: int, seed: int) -> dict[str, float | int | str]:
    # Each setting starts from the same named seed for independent replay.
    rng = np.random.default_rng(seed)
    a = correlated_profile(rng, draws, N_DIMS, rho)
    b = correlated_profile(rng, draws, N_DIMS, rho)
    a_dom_b = np.all(a >= b, axis=1) & np.any(a > b, axis=1)
    b_dom_a = np.all(b >= a, axis=1) & np.any(b > a, axis=1)
    rate = float(np.mean(a_dom_b | b_dom_a))
    se = math.sqrt(rate * (1 - rate) / draws)
    return {
        "model": "five_category_gaussian_copula",
        "dimensions": N_DIMS,
        "rho": rho,
        "draws": draws,
        "seed": seed,
        "numpy_version": np.__version__,
        "bit_generator": "PCG64",
        "rate": rate,
        "standard_error": se,
        "ci95_lower": max(0.0, rate - 1.96 * se),
        "ci95_upper": min(1.0, rate + 1.96 * se),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--draws", type=int, default=DEFAULT_DRAWS)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--json", type=Path, default=Path("stage_b_yield_simulation_v6_2.json"))
    parser.add_argument("--csv", type=Path, default=Path("stage_b_yield_simulation_v6_2.csv"))
    args = parser.parse_args()

    rows: list[dict[str, float | int | str]] = []
    for n in (4, 6, 8, 12):
        rows.append({
            "model": "five_category_independent_exact",
            "dimensions": n,
            "rho": 0.0,
            "draws": "exact",
            "seed": "not_applicable",
            "numpy_version": np.__version__,
            "bit_generator": "not_applicable",
            "rate": exact_k_category_dominance(5, n),
            "standard_error": 0.0,
            "ci95_lower": exact_k_category_dominance(5, n),
            "ci95_upper": exact_k_category_dominance(5, n),
        })
    rows.append({
        "model": "mixed_restriction_exact",
        "dimensions": 12,
        "rho": 0.0,
        "draws": "exact",
        "seed": "not_applicable",
        "numpy_version": np.__version__,
        "bit_generator": "not_applicable",
        "rate": exact_mixed_dominance(5, 7),
        "standard_error": 0.0,
        "ci95_lower": exact_mixed_dominance(5, 7),
        "ci95_upper": exact_mixed_dominance(5, 7),
    })
    rows.append({
        "model": "binary_restriction_exact",
        "dimensions": 12,
        "rho": 0.0,
        "draws": "exact",
        "seed": "not_applicable",
        "numpy_version": np.__version__,
        "bit_generator": "not_applicable",
        "rate": exact_k_category_dominance(2, 12),
        "standard_error": 0.0,
        "ci95_lower": exact_k_category_dominance(2, 12),
        "ci95_upper": exact_k_category_dominance(2, 12),
    })
    rows.extend(simulate(rho, args.draws, args.seed) for rho in (0.30, 0.60))

    args.json.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    with args.csv.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(json.dumps(row, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
