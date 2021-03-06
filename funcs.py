import streamlit as st
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def prediction(model, SepalLength, SepalWidth, PetalLength, PetalWidth):
    """This function returns the preddicted value."""
    species = model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
    species = species[0]
    if species == 0:
        return "Iris_setosa"
    elif species == 1:
        return "Iris-virginica"
    else:
        return "Iris-versicolor"

def svc_score(X_train, y_train, kernel='linear', C=1, gamma='scale', degree=3):
    """This function process svc model"""
    svc_model = SVC(kernel=kernel, C=C, gamma=gamma, degree=degree)
    svc_model.fit(X_train, y_train)
    score = svc_model.score(X_train, y_train)
    return svc_model, score


def rf_score(X_train, y_train, n_estimators=100, max_depth=None):
    """This function process rf_clf model"""
    rf_clf = RandomForestClassifier(n_jobs=-1, n_estimators=n_estimators, max_depth=max_depth)
    rf_clf.fit(X_train, y_train)
    score = rf_clf.score(X_train, y_train)
    return rf_clf, score

def lr_score(X_train, y_train, C=1):
    """This function process rf_clf model"""
    log_reg = LogisticRegression(n_jobs=-1, C=C)
    log_reg.fit(X_train, y_train)
    score = log_reg.score(X_train, y_train)
    return log_reg, score

def clf_s(clf, X_train, y_train):
    if clf == 'Support Vector Machine':
        return svc_score(X_train, y_train)
    elif clf == 'Logistic Regression':
        return lr_score(X_train, y_train)
    else:
        return rf_score(X_train, y_train)