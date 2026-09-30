# Phishing URL Detection

Defensive classification of phishing-related website features using a public UCI benchmark.

Dataset: UCI Phishing Websites, ID 327.

Run `pip install -r requirements.txt`, then `python train.py`. The script downloads the dataset through `ucimlrepo`, scales features, trains a Random Forest and saves the model.

Use this as a triage experiment. Do not treat a prediction as proof that a live URL is safe.