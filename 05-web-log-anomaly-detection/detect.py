import os,pandas as pd
from sklearn.ensemble import IsolationForest
path='data/access.csv'
if not os.path.exists(path): raise SystemExit('Create data/access.csv from an authorized web log first.')
df=pd.read_csv(path); numeric=df.select_dtypes(include='number').columns
if len(numeric)<2: raise SystemExit('Need at least two numeric request features.')
m=IsolationForest(n_estimators=200,contamination='auto',random_state=42); df['anomaly']=m.fit_predict(df[numeric].fillna(0)); df['anomaly_score']=m.decision_function(df[numeric].fillna(0)); df.to_csv('data/scored_access.csv',index=False); print(df['anomaly'].value_counts()); print(df.sort_values('anomaly_score').head(10))
