import os,joblib
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
os.makedirs('models',exist_ok=True); ds=fetch_ucirepo(id=94); X=ds.data.features; y=ds.data.targets.iloc[:,0]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,stratify=y,random_state=42); m=Pipeline([('imp',SimpleImputer(strategy='median')),('scale',StandardScaler()),('model',LogisticRegression(max_iter=1500,class_weight='balanced'))]); m.fit(Xtr,ytr); print(classification_report(yte,m.predict(Xte))); joblib.dump(m,'models/spam_lr.joblib')
