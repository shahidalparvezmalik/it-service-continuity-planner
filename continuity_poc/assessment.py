"""Deterministic, review-only continuity readiness assessment."""
from datetime import date


def assess(records, as_of=None):
    as_of = as_of or date.today()
    results = []
    seen = set()
    for row in records:
        sid = row["service_id"].strip()
        if not sid or sid in seen:
            raise ValueError(f"missing or duplicate service_id: {sid!r}")
        seen.add(sid)
        flags = []
        rto = float(row["rto_hours"])
        rpo = float(row["rpo_hours"])
        tested = row["last_test_date"].strip()
        target = date.fromisoformat(row["next_test_due"])
        last = date.fromisoformat(tested) if tested else None
        if rto <= 0 or rpo < 0:
            raise ValueError(f"invalid recovery objectives for {sid}")
        if not row["owner"].strip(): flags.append("missing_owner")
        if not row["dependency_map_confirmed"].strip().lower() == "yes": flags.append("dependency_map_unconfirmed")
        if not row["backup_evidence"].strip().lower() == "yes": flags.append("backup_evidence_missing")
        if not last: flags.append("recovery_test_not_recorded")
        elif (as_of - last).days > 365: flags.append("recovery_test_overdue")
        if target < as_of: flags.append("next_test_date_overdue")
        results.append({"service_id": sid, "service_name": row["service_name"], "rto_hours": rto, "rpo_hours": rpo, "flag_count": len(flags), "flags": ";".join(flags) or "none", "human_review_required": "yes", "actions_executed": 0})
    return results
