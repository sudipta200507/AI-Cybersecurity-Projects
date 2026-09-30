# Network Intrusion Detection

Build a supervised intrusion detector from the KDD Cup 1999 benchmark.

UCI documents this dataset as a network-intrusion detection task with normal connections and simulated attacks.

Run `pip install -r requirements.txt` then `python train.py`. The script fetches the UCI dataset, one-hot encodes categorical fields and trains a Random Forest binary classifier.

Study class imbalance, categorical network features, confusion matrices and false positives.