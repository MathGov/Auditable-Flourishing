#!/usr/bin/env python3
"""Exploratory AF v6.2 perturbation sensitivity simulation.

Assumptions are deliberately explicit and non-controlling: admitted proposals
are treated as conditionally independent destabilization opportunities. Real
studies must estimate dependence and use the observed replay register.
"""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import numpy as np

def simulate(draws,seed,base_dominance,q,admission_rate,destabilize):
 rng=np.random.default_rng(seed)
 base=rng.random(draws)<base_dominance
 proposed=rng.poisson(q,draws)
 admitted=rng.binomial(proposed,admission_rate)
 stable=np.array([not np.any(rng.random(n)<destabilize) if n else True for n in admitted])
 reported=base & stable
 return {'draws':draws,'seed':seed,'base_dominance':base_dominance,'mean_proposals_q':q,'admission_rate':admission_rate,
         'destabilization_probability_t':destabilize,'reported_dominance_rate':float(reported.mean()),
         'base_dominance_rate_observed':float(base.mean()),'assumption':'conditionally independent exploratory sensitivity; not a protocol rule or empirical forecast'}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--draws',type=int,default=200000); ap.add_argument('--seed',type=int,default=20260812); ap.add_argument('--json',type=Path,default=Path('perturbation_sensitivity_v6_2.json')); ap.add_argument('--csv',type=Path,default=Path('perturbation_sensitivity_v6_2.csv')); a=ap.parse_args()
 rows=[]
 for q in (0.5,1,2,4):
  for admission in (0.25,0.5,0.75):
   for t in (0.05,0.15,0.30): rows.append(simulate(a.draws,a.seed+len(rows),0.10,q,admission,t))
 a.json.write_text(json.dumps(rows,indent=2)+'\n');
 with a.csv.open('w',newline='') as f: w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
 print(json.dumps({'rows':len(rows),'draws_per_row':a.draws},sort_keys=True))
if __name__=='__main__': main()
