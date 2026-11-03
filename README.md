# IT Service Continuity & Recovery Readiness

A small, runnable proof of concept for reviewing service recovery information before a continuity or disaster-recovery exercise.

> This is a deterministic rules demo using fictional records. It is not a business continuity plan, disaster-recovery platform, or assurance of recoverability. It does not connect to infrastructure, validate backups, test recovery, or execute actions. Every result needs human review.

## What it checks

The report flags a missing service owner, an unconfirmed dependency map, missing backup evidence, an absent or older-than-one-year recovery test date, and an overdue next-test date. RTO and RPO are shown as supplied; the tool does not decide whether they are appropriate or achievable.

## Run

Requires Python 3.10+; no third-party packages.

```bash
python -m unittest discover -v
python -m continuity_poc.cli --input data/services.csv --output reports/readiness.csv --as-of 2026-11-03
```

The fixed date makes the synthetic example repeatable. Omit `--as-of` to use the current date.

## Data

`data/services.csv` contains five fictional service records. Fields include service identifier/name, criticality, owner, RTO/RPO, dependency-map and backup-evidence indicators, last recovery-test date, and next test due date. These indicators are user-supplied assertions in the fixture, not evidence validated by software.

## Governance limits

The project does not calculate business impact, define recovery objectives, prioritize services, recommend failover, certify compliance, or determine that a service can be restored. Teams would need approved impact-analysis methods, service-owner confirmation, evidence review, risk acceptance, and tested plans before making operational decisions. No real data should be entered.

## Repository layout

- `continuity_poc/`: assessment rules and CSV CLI
- `data/services.csv`: fictional input
- `tests/`: unit tests
- `docs/DATA_DICTIONARY.md`: field definitions and boundaries
- `docs/OPERATING_MODEL.md`: suggested human review sequence
- `docs/LINKEDIN_ARTICLE.md`: copy-ready article draft
- `docs/LINKEDIN_SHORT_POST.md`, `LINKEDIN_GROUPS_POST.md`: promotional drafts

## Disclaimer

Portfolio proof of concept only. The output is not recovery evidence, audit evidence, a risk acceptance, or professional continuity advice.
