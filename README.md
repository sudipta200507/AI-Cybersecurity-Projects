# AI + Cybersecurity Projects

Defensive AI projects for security detection, classification, triage and anomaly analysis. The repository focuses on **authorized, evidence-driven security engineering**.

## Project map

| Project | Security problem | Approach | Dataset |
|---|---|---|---|
| 01 | Phishing website detection | Random Forest | UCI Phishing Websites |
| 02 | Network intrusion detection | Random Forest | KDD Cup 1999 / UCI ID 130 |
| 03 | Firewall action classification | Random Forest | UCI Internet Firewall Data ID 542 |
| 04 | Email spam triage | Logistic Regression | UCI Spambase ID 94 |
| 05 | Web-log anomaly detection | Isolation Forest | Authorized/local logs |

## Exact dataset sources

- Phishing Websites — https://archive.ics.uci.edu/dataset/327/phishing — direct archive: https://archive.ics.uci.edu/static/public/327/phishing+websites.zip
- KDD Cup 1999 — official KDD Cup data page: https://kdd.org/kdd-cup/view/kdd-cup-1999/Data — full archive: https://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz — 10% archive: https://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz
- UCI KDD Cup 1999 — https://archive.ics.uci.edu/dataset/130/kdd+cup+1999+data
- Internet Firewall Data — UCI ID 542: https://archive.ics.uci.edu/dataset/542/internet+firewall+data
- Spambase — UCI ID 94: https://archive.ics.uci.edu/dataset/94/spambase

The KDD Cup official data page provides both the full dataset and a 10% subset, with the full archive listed as 18 MB compressed and 743 MB uncompressed. citeturn0search0turn0search13

## Security boundary

These projects are for defensive analysis and authorized environments. They do not automate exploitation, credential theft, destructive actions or unauthorized access. Model output is evidence for analyst review—not an unconditional security verdict.

## Engineering workflow

**raw evidence → parsing/feature extraction → validation → model → metrics → saved artifact → analyst-facing inference**

## Why this repository matters

Security ML is not just calling a classifier. The important engineering questions are: what evidence enters the model, what features represent an attack, how class imbalance affects detection, what false positives cost, and how an analyst can reproduce the result.

## Reproducibility

Each benchmark project documents its official source, setup, training command, evaluation metrics and limitations. The log-anomaly project intentionally requires a locally supplied authorized log rather than bundling real-world sensitive traffic.
