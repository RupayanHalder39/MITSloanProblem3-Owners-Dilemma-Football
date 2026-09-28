# Public Release Audit

## Release scope

- Source master project: local read-only research workspace for the Owner's Dilemma study.
- Publication source: final two-page Problem 3 paper.
- Public repository: `RupayanHalder39/MITSloanProblem3-Owners-Dilemma-Football`.
- Reproducibility status: partial.

## Included artifacts

- Final paper under a clean public filename.
- Final conceptual sporting-financial framework figure in PNG and SVG formats.
- Final post-hoc robustness figure in PNG and SVG formats.
- Aggregate validation, held-out, and robustness metrics.
- Public-safe figure-generation and release-validation scripts.
- Methodology, data-provenance, reproducibility, and limitation documentation.
- Researcher photograph and collaboration logo supplied for the release.

## Intentionally excluded artifacts

- Raw, interim, processed, and row-level datasets.
- Database, Parquet, model-serialization, and cache files.
- Club-level predictions and other row-level outputs.
- Internal project logs, planning documents, reviewer material, and earlier manuscripts.
- Exploratory figures, superseded results, dependency folders, and local caches.

## Data redistribution decision

No raw or row-level data are distributed. The published transaction snapshot declares CC0, but the
project audit records unresolved upstream redistribution and commercial-use questions. Sporting
records also require separate authorization. The public package therefore provides aggregate
results and reconstruction documentation without implying rights to third-party data.

## Provenance handling

Publication-facing prose uses the neutral description “published transfer-transaction dataset.”
`docs/data_provenance.md` preserves exact technical attribution because accurate provenance must not
be obscured. Known-fee transfer balance is consistently defined as known sales fees minus known
purchase fees and is not described as accounting profit.

## Scientific consistency checks

- Sample: 159 club-window observations across 2017-18 through 2024-25.
- Split: 99 training, 40 validation, and 20 held-out observations; held-out season 2024-25.
- Validation MAE: B2 0.219931; richer model 0.226723.
- Held-out MAE: mean 0.361310; persistence 0.271571; B2 0.238262; richer model 0.240975.
- Richer minus persistence: -0.030596 PPG MAE.
- Richer minus B2: +0.002713 PPG MAE.
- All eight robustness values agree with the authoritative Stage 7/8 artifacts.
- The +/-0.02 PPG region is described only as a practical comparison band.
- Robustness analyses are labelled post-hoc and not independent validation.
- The Pareto frontier is labelled conceptual and not empirically estimated.

## Validation and safety checks

- `python scripts/verify_release.py`: PASS.
- `python src/build_figures.py`: PASS; both publication figures regenerated from public inputs.
- Python source compilation: PASS.
- `CITATION.cff` YAML parsing: PASS.
- README relative-link check: PASS; seven local links resolved.
- Final paper check: PASS; two A4 pages and all headline values present.
- Secret and credential scan: PASS.
- Restricted-file and row-level-data scan: PASS.
- Symlink scan: PASS.
- Portability scan: PASS; no machine-specific dependency appears in release content.
- Large-file scan: PASS; no file exceeds 25 MB.
- Staged-path inspection: PASS; 21 intended release files, no restricted extensions or unexpected
  artifacts.

## Git publication

- Content release commit: pending creation after this audit snapshot.
- Remote: `https://github.com/RupayanHalder39/MITSloanProblem3-Owners-Dilemma-Football.git`
- Remote preflight: reachable and empty.
- Push status: pending.

## Remaining limitations

Independent end-to-end model reproduction is not possible without authorized source data. The
public package reproduces the aggregate checks and final figures and documents the required schema
and scientific boundaries.
