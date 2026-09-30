import joblib
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
ds=fetch_ucirepo(id=130); X=ds.data.features.copy(); y=ds.data.targets.iloc[:,0].astype(str).str.lower().eq('normal').astype(int)
_,Xtest,_,ytest=train_test_split(X,y,test_size=.2,stratify=y,random_state=42); model=joblib.load('models/intrusion_rf.joblib'); pred=model.predict(Xtest)
print(classification_report(ytest,pred)); print('Confusion matrix:\n',confusion_matrix(ytest,pred))