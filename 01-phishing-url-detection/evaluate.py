import joblib
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,roc_auc_score
ds=fetch_ucirepo(id=327); X=ds.data.features; y=ds.data.targets.iloc[:,0]
_,Xtest,_,ytest=train_test_split(X,y,test_size=.2,stratify=y,random_state=42); model=joblib.load('models/phishing_rf.joblib'); pred=model.predict(Xtest)
print(classification_report(ytest,pred)); print(confusion_matrix(ytest,pred))
try: print('ROC-AUC:',roc_auc_score(ytest,model.predict_proba(Xtest)[:,1]))
except ValueError: pass