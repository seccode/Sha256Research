import hashlib
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Simplified Sha2 hash
def hash2(s):
    h = hashlib.sha256()
    h.update(s.encode("utf-8", "replace"))
    return h.hexdigest()[0] in "01234567"

if __name__ == "__main__":
    m=0
    s=open("proof.py").read()
    c="e"
    # Build new x, y on each iteration
    x, y = [], []
    for j in range(len(s)):
        x.append(j)
        y.append(hash2(s[:j]+c+s[j:]))
    print(max(y.count(0),y.count(1))/len(y))
    for i in range(100_000_000):
        x=np.array(x).reshape(-1,1)
        x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.5, stratify=y)

        clf=RandomForestClassifier()
        clf.fit(x_train,y_train)
        m += clf.score(x_test,y_test)
        print(i,m/(i+1))

