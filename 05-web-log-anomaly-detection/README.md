# Web Log Anomaly Detection

## Goal
Detect unusual request patterns in an authorized web-access log using an unsupervised anomaly detector.

## Dataset
No third-party dataset is required. The repository intentionally expects an **authorized local log** at `data/access.csv` because real web logs can contain sensitive identifiers and customer information.

Expected numeric features can include request count, status code, bytes, response time or other privacy-reviewed aggregates.

## Pipeline
Authorized log → schema validation → numeric feature selection → missing-value handling → Isolation Forest → anomaly score → analyst review file.

## Run
`pip install -r requirements.txt`

Create `data/access.csv`, then run `python detect.py`.

The script writes `data/scored_access.csv` and exposes both the binary anomaly flag and continuous anomaly score.

## Why Isolation Forest?
It provides an unsupervised baseline when reliable attack labels are unavailable.

## Production considerations
Add timestamp-aware windows, baseline learning, drift detection, authentication-aware features, privacy controls and alert suppression. Never treat an anomaly as proof of malicious activity.
