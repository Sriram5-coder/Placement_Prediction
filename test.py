from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
import pandas as pd
import random


# Load dataset
def load_data():
    df = pd.read_csv("dataset.csv")
    return df


# Preprocess data
def preprocess_data(df):
    X = df.drop(columns=["label"])
    y = df["label"]
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y


# Load and preprocess data
df = load_data()
X, y = preprocess_data(df)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# Define your function to check accuracy
def check_accuracy(selected_classifier, model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    if accuracy < 0.89:
        # Encrypt the accuracy value
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_accuracy = cipher_suite.encrypt(str(accuracy).encode())
        return encrypted_accuracy.decode()  # Return the encrypted accuracy
    else:
        return accuracy
from cryptography.fernet import Fernet
import random
from sklearn.metrics import accuracy_score
# Iterate over classifiers
for clf_name, clf in classifiers.items():
    # Fit the classifier
    clf.fit(X_train, y_train)

    # Calculate accuracy and check if it's above 90%
    check_a = check_accuracy(clf_name, clf, X_train, y_train, X_test, y_test)
    if isinstance(check_a, float) and check_a >= 0.90:
        print(f"The accuracy of {clf_name} model is: {check_a:.2f}")
    else:
        print(f"The accuracy of {clf_name} model is below 90% and is encrypted.")
        print(f"The encrypted accuracy: {check_a}")

# # Define your function to check accuracy
# def check_accuracy(selected_classifier, model, X_train, y_train, X_test, y_test):
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)

#     if accuracy < 0.89:
#         # Encrypt the accuracy value
#         key = Fernet.generate_key()
#         cipher_suite = Fernet(key)
#         encrypted_accuracy = cipher_suite.encrypt(str(accuracy).encode())
#         return encrypted_accuracy.decode()  # Return the encrypted accuracy
#     else:
#         return accuracy


# Define classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(max_iter=100000),  # Increase max_iter
    "Decision Tree": DecisionTreeClassifier(max_depth=7),  # Increase max_depth
    "Naive Bayes": GaussianNB(),
    "Random Forest": RandomForestClassifier(
        n_estimators=200, max_depth=10
    ),  # Increase n_estimators and max_depth
}

# Iterate over classifiers
for clf_name, clf in classifiers.items():
    # Fit the classifier
    clf.fit(X_train, y_train)

    # Predict and calculate accuracy
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    check_a = check_accuracy(clf_name, clf, X_train, y_train, X_test, y_test)

    # Print accuracy
    print(f"The accuracy of {clf_name} model is: {accuracy:.2f}")
    print(f"The accuracy of {clf_name} model is: {check_a}")
