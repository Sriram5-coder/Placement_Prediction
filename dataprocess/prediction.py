import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

data = pd.read_csv("dataset.csv")
data = data.dropna()
X = data.drop(columns=["selected"])
y = data["selected"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(
    "\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=1)
)
dump(classifier, "random_forest_model.joblib")
