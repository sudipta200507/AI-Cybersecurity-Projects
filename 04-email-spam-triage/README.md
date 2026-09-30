# Email Spam Triage

## Goal
Build a defensive baseline for identifying unsolicited email from engineered message features.

## Dataset
**UCI Spambase, ID 94.**
Official: https://archive.ics.uci.edu/dataset/94/spambase
Files: https://archive-beta.ics.uci.edu/dataset/94/spambase/files

## Pipeline
UCI features → imputation → scaling → class-balanced Logistic Regression → precision/recall/F1 → model artifact.

## Why Logistic Regression?
It gives an interpretable probability-based baseline and makes threshold tuning straightforward.

## Run
`pip install -r requirements.txt`
`python train.py`

## Security boundary
This project classifies engineered features; it does not open attachments, execute content or perform malware analysis.

## Extensions
Add text-based NLP, header analysis, attachment metadata, calibration, analyst explanations and integration with an email-ingestion pipeline such as the one developed in ForentisAI.