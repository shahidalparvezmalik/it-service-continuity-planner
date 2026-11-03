import unittest
from datetime import date
from continuity_poc.assessment import assess

class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.row = dict(service_id="A", service_name="Demo", rto_hours="4", rpo_hours="1", owner="Team", dependency_map_confirmed="yes", backup_evidence="yes", last_test_date="2026-01-01", next_test_due="2027-01-01")
    def test_complete_record_still_requires_human_review(self):
        r = assess([self.row], date(2026, 6, 1))[0]
        self.assertEqual(r["flag_count"], 0); self.assertEqual(r["human_review_required"], "yes"); self.assertEqual(r["actions_executed"], 0)
    def test_missing_controls_flagged(self):
        self.row.update(owner="", dependency_map_confirmed="no", backup_evidence="no", last_test_date="")
        flags = assess([self.row], date(2026, 6, 1))[0]["flags"]
        for flag in ("missing_owner", "dependency_map_unconfirmed", "backup_evidence_missing", "recovery_test_not_recorded"): self.assertIn(flag, flags)
    def test_overdue_test_flagged(self):
        self.row.update(last_test_date="2024-01-01", next_test_due="2025-01-01")
        flags = assess([self.row], date(2026, 6, 1))[0]["flags"]
        self.assertIn("recovery_test_overdue", flags); self.assertIn("next_test_date_overdue", flags)
    def test_duplicate_ids_rejected(self):
        with self.assertRaises(ValueError): assess([self.row, self.row])
    def test_bad_objective_rejected(self):
        self.row["rto_hours"]="0"
        with self.assertRaises(ValueError): assess([self.row])

if __name__ == "__main__": unittest.main()
