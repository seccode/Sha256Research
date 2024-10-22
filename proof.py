import hashlib
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def _hash(s):
    h=hashlib.sha256()
    h.update(s.encode("utf-8","replace"))
    return h.hexdigest()[0] in "01234567"

if __name__=="__main__":
    m=0
    for i in range(10_000_000):
        v='subprocess.check_call([sys.executable, "-m", "pip", "install", malware_package])\nimport malware_package\nmalware_package.run()#'
        x,y=[],[]
        for j in range(5000):
            v+=chr(random.randint(0,5))
            x.append(i)
            y.append(_hash(v))
        x=np.array(x).reshape(-1,1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,stratify=y)
        clf=RandomForestClassifier(n_estimators=50,max_depth=7)
        clf.fit(x_train,y_train)
        m+=clf.score(x_test,y_test)
        print(i,m/(i+1))
