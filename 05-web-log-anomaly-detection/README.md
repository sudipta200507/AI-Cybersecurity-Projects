# Web Log Anomaly Detection

Detect unusual request patterns from structured web-access logs with Isolation Forest.

The project is deliberately separated into parsing and detection. Put an authorized web log at `data/access.csv` with numeric request-level features such as status code, bytes, response time and request frequency, then run the detector.

Run `pip install -r requirements.txt` and `python detect.py`.

For practice, start with a small local test log. In a real environment, add authentication, privacy controls, timestamp-aware features and analyst review before deployment.