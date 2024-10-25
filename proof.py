import hashlib
import itertools
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from tqdm import tqdm

def _hash(s):
    h=hashlib.sha256()
    h.update(s.encode("utf-8","replace"))
    return h.hexdigest()[1] in "01234567"

if __name__=="__main__":
    x,y=[],[]
    for c in tqdm([chr(j) for j in range(10_000)]):
        x.extend(list(range(len(x),len(x)+1_000)))
        z=c
        for i in range(1_000):
            y.append(_hash(z))
            z+=c
    x=np.array(x).reshape(-1,1)
    print(y.count(1)/len(y))
    m=0
    for i in range(100_000):
        x_train,x_test,y_train,y_test=train_test_split(x,y,stratify=y,test_size=0.95)
        clf=RandomForestClassifier(n_estimators=1,max_depth=1)
        clf.fit(x_train,y_train)
        m+=clf.score(x_test,y_test)
        print(i,m/(i+1))
