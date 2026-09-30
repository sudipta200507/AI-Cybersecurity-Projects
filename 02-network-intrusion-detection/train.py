import os,joblib
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
os.makedirs('models',exist_ok=True); ds=fetch_ucirepo(id=130); X=ds.data.features.copy(); y=ds.data.targets.iloc[:,0].astype(str)
y=(y.str.lower()=='normal').astype(int); cat=X.select_dtypes(include='object').columns; num=X.select_dtypes(exclude='object').columns
prep=ColumnTransformer([('cat',OneHotEncoder(handle_unknown='ignore'),cat)],remainder='passthrough'); m=Pipeline([('prep',prep),('model',RandomForestClassifier(n_estimators=200,class_weight='balanced',random_state=42,n_jobs=-1))]); Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,stratify=y,random_state=42); m.fit(Xtr,ytr); print(classification_report(yte,m.predict(Xte))); joblib.dump(m,'models/intrusion_rf.joblib')
