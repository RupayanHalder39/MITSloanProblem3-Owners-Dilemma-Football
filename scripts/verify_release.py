"""Validate the public release without requiring restricted source data."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


required = [
    "README.md", "LICENSE", "CITATION.cff", "paper/Problem3_The_Owners_Dilemma.pdf",
    "figures/figure_1_owners_dilemma_framework.png", "figures/figure_1_owners_dilemma_framework.svg",
    "figures/figure_2_robustness_vs_b2.png", "figures/figure_2_robustness_vs_b2.svg",
    "results/heldout_metrics.csv", "results/robustness_vs_b2.csv", "docs/methodology.md",
    "docs/data_provenance.md", "docs/reproducibility.md", "docs/limitations.md",
]
for rel in required:
    check((ROOT / rel).is_file(), f"missing required file: {rel}")

metrics = {(row["partition"], row["model"]): float(row["mae_ppg"])
           for row in read_csv("results/heldout_metrics.csv")}
expected_metrics = {
    ("validation", "B2 prior-strength baseline"): 0.219931,
    ("validation", "Richer transfer-window model"): 0.226723,
    ("held-out test", "Mean PPG"): 0.361310,
    ("held-out test", "Persistence"): 0.271571,
    ("held-out test", "B2 prior-strength baseline"): 0.238262,
    ("held-out test", "Richer transfer-window model"): 0.240975,
}
for key, expected in expected_metrics.items():
    check(key in metrics and abs(metrics[key] - expected) < 5e-7, f"metric mismatch: {key}")
if all(key in metrics for key in expected_metrics):
    persistence_delta = metrics[("held-out test", "Richer transfer-window model")] - metrics[("held-out test", "Persistence")]
    b2_delta = metrics[("held-out test", "Richer transfer-window model")] - metrics[("held-out test", "B2 prior-strength baseline")]
    check(abs(persistence_delta - (-0.030596)) < 1e-6, "richer-minus-persistence mismatch")
    check(abs(b2_delta - 0.002713) < 1e-6, "richer-minus-B2 mismatch")

robustness = {row["variant"]: float(row["variant_mae_minus_b2_mae_ppg"])
              for row in read_csv("results/robustness_vs_b2.csv")}
expected_robustness = {
    "Frozen full model": 0.002713, "Green-fee rows only": 0.020235,
    "Excluding 2020-21": 0.002024, "Post-window-close target": -0.003229,
    "Separate sales + purchases": 0.003278, "Prior strength + balance": -0.002869,
    "No balance": 0.005258, "Prior strength + movements": 0.005163,
}
for label, expected in expected_robustness.items():
    check(label in robustness and abs(robustness[label] - expected) < 5e-7,
          f"robustness mismatch: {label}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for fragment in ["159 La Liga", "99 training", "40 validation", "20-club held-out",
                 "2017-18", "2024-25", "0.219931", "0.226723", "0.361310",
                 "0.271571", "0.238262", "0.240975", "0.030596", "0.002713"]:
    check(fragment in readme, f"README missing headline fragment: {fragment}")
check("Transfermarkt" not in readme, "publication-facing README contains prohibited source name")
check("/Users/" not in readme, "README contains an absolute local path")

restricted_suffixes = {".duckdb", ".db", ".sqlite", ".sqlite3", ".parquet", ".joblib", ".pkl"}
for path in ROOT.rglob("*"):
    if path.is_symlink():
        ERRORS.append(f"symlink not allowed: {path.relative_to(ROOT)}")
    if path.is_file() and path.suffix.lower() in restricted_suffixes:
        ERRORS.append(f"restricted file type present: {path.relative_to(ROOT)}")
    if path.is_file() and path.stat().st_size > 25 * 1024 * 1024:
        ERRORS.append(f"unexpected large file: {path.relative_to(ROOT)}")
    if path.is_file() and path.suffix.lower() in {".md", ".py", ".csv", ".cff", ".txt"}:
        text = path.read_text(encoding="utf-8", errors="replace")
        local_prefix = "/" + "Users/rupayan/"
        check(local_prefix not in text, f"absolute local path in {path.relative_to(ROOT)}")
        check(not re.search(r"AKIA[0-9A-Z]{16}", text), f"possible AWS key in {path.relative_to(ROOT)}")

if ERRORS:
    print("PUBLIC RELEASE VERIFICATION: FAIL")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("PUBLIC RELEASE VERIFICATION: PASS")
print("Sample: 159 club-window observations; 99 train, 40 validation, 20 held-out")
print("Held-out MAE: mean 0.361310; persistence 0.271571; B2 0.238262; richer 0.240975")
print("Reproduction status: PARTIAL (aggregate outputs and figures only)")
