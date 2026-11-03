import argparse, csv
from datetime import date
from pathlib import Path
from .assessment import assess

p = argparse.ArgumentParser(description="Review synthetic service continuity records")
p.add_argument("--input", default="data/services.csv")
p.add_argument("--output", default="reports/readiness.csv")
p.add_argument("--as-of", type=date.fromisoformat)
a = p.parse_args()
with open(a.input, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
results = assess(rows, a.as_of)
out = Path(a.output); out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=results[0].keys()); w.writeheader(); w.writerows(results)
print(f"Services assessed: {len(results)}")
print(f"Services with review flags: {sum(x['flag_count'] > 0 for x in results)}")
print("Human review required: yes; recovery actions executed: 0")
print(f"Report: {out}")
