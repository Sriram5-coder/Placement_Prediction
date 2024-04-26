import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import pickle


crop_data = pd.read_csv("dataset.csv")


X = crop_data.drop(columns=['label'])
y = crop_data["label"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


log_reg = LogisticRegression(solver="liblinear", random_state=2).fit(
    X_train_scaled, y_train
)


decision_tree = DecisionTreeClassifier(
    criterion="entropy", random_state=2, max_depth=5
).fit(X_train, y_train)
naive_bayes = GaussianNB().fit(X_train, y_train)
random_forest = RandomForestClassifier(n_estimators=20, random_state=0).fit(
    X_train, y_train
)


with open("LR_model.pkl", "wb") as file:
    pickle.dump(log_reg, file)

with open("DT_model.pkl", "wb") as file:
    pickle.dump(decision_tree, file)

with open("NaiveBayes_model.pkl", "wb") as file:
    pickle.dump(naive_bayes, file)

with open("RF_model.pkl", "wb") as file:
    pickle.dump(random_forest, file)
