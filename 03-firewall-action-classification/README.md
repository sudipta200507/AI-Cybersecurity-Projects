# Firewall Action Classification

## Goal
Classify firewall traffic into the action classes recorded in a public university-firewall dataset.

## Dataset
**UCI Internet Firewall Data, ID 542.**
Official: https://archive.ics.uci.edu/dataset/542/internet+firewall+data

UCI documents 65,532 records and four action classes from university firewall traffic.

## Pipeline
Official tabular data → train/test split → Random Forest → multiclass metrics → serialized model.

## Why this matters
Firewall automation is a decision-support problem. A false block and a missed malicious flow have different operational costs. Accuracy alone is therefore not enough.

## Run
`pip install -r requirements.txt`
`python train.py`

## Extensions
Add per-class recall, macro-F1, confusion matrices, probability calibration and a policy layer that separates model prediction from the final firewall action.