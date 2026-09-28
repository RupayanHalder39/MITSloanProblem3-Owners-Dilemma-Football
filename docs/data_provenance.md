# Data provenance and availability

## Sporting outcomes

The sporting backbone was supplied for research use through the project collaboration. Raw and
row-level sporting records are not included in this public repository.

## Transfer transactions

The research used a frozen published `dcaribou/transfermarkt-datasets` snapshot derived from
Transfermarkt. The project performed no direct scraping. The published snapshot declares CC0, but
the research audit records unresolved upstream redistribution and commercial-use questions.
Published fee values may be reported or estimated rather than official final cash consideration.

For those reasons, the snapshot, derived row-level transaction records, databases, and analytical
club-window dataset are excluded from this release. This attribution is retained here for accurate
technical provenance; publication-facing narrative uses the neutral description “published
transfer-transaction dataset.”

## Reconstruction by an authorized researcher

An authorized researcher can reconstruct the analytical inputs by obtaining permitted copies of:

1. match outcomes sufficient to calculate associated-season La Liga PPG;
2. the exact published transfer-transaction snapshot used by the study;
3. summer-window dates and club identity mappings; and
4. the documented fields needed to construct prior strength, promotion status, known-fee balance,
   movement counts, fee coverage, and the COVID-era indicator.

The required final schema is one row per club and summer window, with season, club identifier,
associated-season PPG, prior strength, promotion status, known sales fees, known purchase fees,
known-fee balance, incoming and outgoing movement counts, fee-coverage measures, and context flags.

No license in this repository grants rights to excluded or third-party data.
