# Data dictionary

| Field | Meaning | Boundary |
|---|---|---|
| service_id | Fictional unique service key | Duplicate and blank values are rejected |
| service_name | Fictional service label | Descriptive only |
| criticality | Fixture label for service importance | Not interpreted or ranked by code |
| owner | Named role/team in the fictional record | Blank value triggers review |
| rto_hours | Supplied recovery time objective | Displayed, not validated against capability |
| rpo_hours | Supplied recovery point objective | Displayed, not validated against backup design |
| dependency_map_confirmed | Whether fixture says dependencies were confirmed | `yes` only avoids the unconfirmed flag; no map is inspected |
| backup_evidence | Whether fixture says evidence is available | Assertion only; no backup is queried or tested |
| last_test_date | ISO date of last recorded exercise | Missing or older than 365 days triggers review |
| next_test_due | ISO date for next exercise | Past date triggers review |

All bundled records are fictional. Never input personal, confidential, or production service data.
