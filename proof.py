import hashlib
import itertools
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def _hash(s):
    h=hashlib.sha256()
    h.update(s.encode("utf-8","replace"))
    return h.hexdigest()[1] in "01234567"

if __name__=="__main__":
    z=0
    x,y=[],[]
    for c in [chr(j) for j in range(65,128)]:
        x.extend(list(range(len(x),len(x)+200)))
        y.extend([_hash("".join(s)) for s in [c*i for i in range(200)]])
        z+=y.count(0)/len(y)
    x=np.array(x).reshape(-1,1)
    print(z/(128-65))
    m=0
    for i in range(100_000):
        x_train,x_test,y_train,y_test=train_test_split(x,y,stratify=y,test_size=0.2)
        clf=RandomForestClassifier(n_estimators=1,max_depth=1)
        clf.fit(x_train,y_train)
        m+=clf.score(x_test,y_test)
        print(i,m/(i+1))
