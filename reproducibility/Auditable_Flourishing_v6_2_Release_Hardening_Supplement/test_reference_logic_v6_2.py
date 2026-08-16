#!/usr/bin/env python3
import json, unittest
from pathlib import Path
from reference_logic_v6_2 import derive_stage_a, perturbation_admitted
ROOT=Path(__file__).resolve().parent
class TestAF62(unittest.TestCase):
 def test_unconditional(self): self.assertEqual(derive_stage_a(["Adequate for scope"]*6),"Stage-A admissible - scoped")
 def test_control_dependent(self): self.assertEqual(derive_stage_a(["Adequate for scope"]*5+["Adequate - control-dependent"]),"Stage-A admissible - scoped, control-dependent")
 def test_unrecognized_refuses(self): self.assertEqual(derive_stage_a(["Adequate for scope"]*5+["Fail"]),"Protocol refusal to evaluate")
 def test_patchable(self): self.assertEqual(derive_stage_a(["Adequate for scope"]*5+["Material defect - patchable"]),"Stage-A non-admissible - patchable")
 def test_unpatchable_controls_over_indeterminate(self):
  states=["Adequate for scope"]*4+["Material defect - unpatchable for stated claim","Indeterminate"]
  self.assertEqual(derive_stage_a(states),"Stage-A non-admissible - unpatchable for stated claim")
 def test_patchable_controls_over_indeterminate(self):
  states=["Adequate for scope"]*4+["Material defect - patchable","Indeterminate"]
  self.assertEqual(derive_stage_a(states),"Stage-A non-admissible - patchable")
 def test_unpatchable_controls_over_unresolved_floor(self):
  states=["Adequate for scope"]*5+["Material defect - unpatchable for stated claim"]
  self.assertEqual(derive_stage_a(states,floor_unresolved=True),"Stage-A non-admissible - unpatchable for stated claim")
 def test_admission(self): self.assertTrue(perturbation_admitted(json.loads((ROOT/'perturbation_record_valid_v6_2.json').read_text())))
 def test_no_private_veto(self):
  r=json.loads((ROOT/'perturbation_record_valid_v6_2.json').read_text()); r['second_reviewer_id']=None; r['adjudicator_id']=None
  self.assertFalse(perturbation_admitted(r))
if __name__=='__main__': unittest.main(verbosity=2)
