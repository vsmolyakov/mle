import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pickle

def train():

    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.5)

    rfc = RandomForestClassifier(n_estimators=10)

    rfc.fit(X_train, y_train)

    predicted = rfc.predict(X_test)

    print(accuracy_score(predicted, y_test))

    with open('./rfc-model.pkl', 'wb') as model_pkl:
        pickle.dump(rfc, model_pkl)

    df_test = pd.DataFrame(X_test, columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    df_test.to_csv("./test-data.csv", index=False)

if __name__ == "__main__":
    train()