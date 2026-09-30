# Email Spam Triage

A defensive ML baseline for prioritising unsolicited email using UCI Spambase.

The dataset contains 4,601 email records and 57 engineered features. Train a Logistic Regression classifier and inspect precision/recall because false positives matter in email filtering.

Run `pip install -r requirements.txt` then `python train.py`.

This is a triage model, not a malware detector. Do not execute attachments or automatically trust its verdict.