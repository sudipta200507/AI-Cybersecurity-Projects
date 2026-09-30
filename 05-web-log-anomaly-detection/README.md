# Web Log Anomaly Detection

## Goal
Detect unusual request patterns in an authorized web-access log using an unsupervised detector.

## Data
No third-party log is bundled. Provide an authorized `data/access.csv` so sensitive production traffic never enters the repository.

## Pipeline
Log → schema validation → numeric feature selection → missing-value handling → Isolation Forest → anomaly flag + continuous score → analyst review.

## Run
`pip install -r requirements.txt`

`python detect.py`

The detector writes `data/scored_access.csv`. An anomaly is an investigation signal, not proof of malicious behaviour.

## Production extensions
Add time-window features, baseline learning, drift detection, identity-aware aggregation, privacy controls, alert deduplication and a human-review workflow.
