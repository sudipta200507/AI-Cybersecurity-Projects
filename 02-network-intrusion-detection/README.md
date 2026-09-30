# Network Intrusion Detection

## Goal
Classify network connections as normal or anomalous using a documented intrusion-detection benchmark.

## Dataset
**KDD Cup 1999.**
Official KDD Cup data page: https://kdd.org/kdd-cup/view/kdd-cup-1999/Data
UCI dataset page: https://archive.ics.uci.edu/dataset/130/kdd+cup+1999+data
Full archive: https://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz
10% archive: https://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz

The official KDD page lists the full 18 MB compressed dataset and a 10% subset. citeturn0search0

## Pipeline
Categorical/numeric network features → encoding → stratified split → class-balanced Random Forest → classification report → model persistence.

## Why this benchmark?
It provides a classic supervised intrusion-detection workload and makes class imbalance, feature representation and false-positive costs visible.

## Run
`pip install -r requirements.txt`
`python train.py`

## Important limitation
KDD Cup 1999 is historical. A modern IDS needs current traffic distributions, encrypted-traffic considerations, drift monitoring and carefully validated labels.

## Extensions
Compare XGBoost/LightGBM-style gradient boosting, anomaly detection, temporal validation, SHAP and alert-threshold optimization.