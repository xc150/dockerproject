#!/usr/bin/env python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_iris(train_fraction=0.8):
    data = load_iris()
    
    X = data.data
    Y = data.target
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=1.-train_fraction)

    lr = LogisticRegression(C=1e5, solver='liblinear')
    lr.fit(X_train, Y_train)

    print("Testing Accuracy:",
            lr.score(X_test, Y_test))

if __name__ == '__main__':
    train_iris()