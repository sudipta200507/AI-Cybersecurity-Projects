import os,joblib
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
os.makedirs('models',exist_ok=True); ds=fetch_ucirepo(id=327); X=ds.data.features; y=ds.data.targets.iloc[:,0]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,stratify=y,random_state=42); m=RandomForestClassifier(n_estimators=300,class_weight='balanced',random_state=42,n_jobs=-1); m.fit(Xtr,ytr); print(classification_report(yte,m.predict(Xte))); joblib.dump(m,'models/phishing_rf.joblib')
