# Methodology

## Unit of analysis and outcome

The analytical unit is a La Liga club-by-summer-window observation. The final sample contains 159
observations across eight seasons, 2017-18 through 2024-25. The target is associated-season league
points per game.

## Chronological design

The study uses 99 training observations, 40 validation observations, and a 20-club held-out test
from 2024-25. Preprocessing choices, metrics, baselines, and model selection were finalized before
the held-out outcomes were used for the principal comparison.

Mean absolute error in PPG is the primary metric. Lower values indicate forecasts closer to the
observed associated-season PPG.

## Predictors and models

The transparent baselines are mean PPG, persistence, and B2, a compact prior-strength baseline. The
richer ordinary-least-squares model combines prior strength, promotion status, known-fee transfer
balance, movement counts, fee coverage, and COVID-era context.

Known-fee transfer balance is known sales fees minus known purchase fees. It is a transaction
measure, not accounting profit. Missing fees remain unknown rather than being interpreted as zero
or free transfers.

## Robustness analyses

The public robustness table reports variant MAE minus B2 MAE. Negative values favor the richer
variant and positive values favor B2. The +/-0.02 PPG region is a practical comparison band, not a
confidence interval or statistical equivalence interval. These checks are post-hoc and do not
constitute independent validation.

## Claim boundary

The design is predictive and observational. It supports comparisons of forecast error but not
causal claims about transfers. The conceptual Pareto frontier is an explanatory framework and was
not estimated from the analytical sample.
