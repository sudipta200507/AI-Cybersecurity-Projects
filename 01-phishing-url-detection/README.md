# Phishing URL Detection

## Goal
Build a defensive classifier for phishing-related website features.

## Dataset
UCI Phishing Websites, ID 327.
Official: https://archive.ics.uci.edu/dataset/327/phishing
Direct archive: https://archive.ics.uci.edu/static/public/327/phishing+websites.zip

UCI reports 11,055 instances and 30 integer features. citeturn0search3

## Pipeline
Dataset → train/test split → Random Forest → precision/recall/F1 → saved model.

## Why Random Forest?
It provides a strong non-linear tabular baseline and exposes feature importance for later explainability work.

## Run
`pip install -r requirements.txt`
`python train.py`

## Security interpretation
The classifier is a benchmark detector, not a live URL reputation service. Production detection would require fresh threat intelligence, domain/WHOIS/DNS features, adversarial evaluation and analyst review.

## Extensions
Add cross-validation, calibrated probabilities, SHAP explanations, current URL feeds and a FastAPI inference layer.