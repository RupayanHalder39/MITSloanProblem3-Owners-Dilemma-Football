# Reproducibility

## Public reproduction scope

This repository provides partial reproduction from frozen aggregate outputs. It verifies headline
metrics and regenerates the two publication figures without requiring raw or row-level records.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_release.py
python src/build_figures.py
```

`scripts/verify_release.py` checks the sample design, validation and held-out metrics, model
differences, robustness values, file inventory, links, portability, symlinks, restricted file
extensions, and selected safety patterns.

`src/build_figures.py` recreates the conceptual framework and robustness figure. The conceptual
frontier and choices are illustrative. The robustness figure reads
`results/robustness_vs_b2.csv`.

## Full reconstruction limitation

Full model refitting is not possible from this repository because the source data and derived
row-level analytical dataset are intentionally excluded. Authorized researchers should reconstruct
the club-window table using the fields in `docs/data_provenance.md`, preserve chronological splits,
and evaluate against the documented aggregate values without altering expected constants.
