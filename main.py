import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


# Load dataset
# @st.cache
def load_data():
    df = pd.read_csv("dataset.csv")
    return df


df = load_data()


# Split dataset into training and testing sets
X = df.drop(columns=["label"])
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train models
models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=21, criterion="entropy"),
    "Random Forest": RandomForestClassifier(n_estimators=300, max_depth=30),
}


# Define function to predict top companys
# "Logistic Regression" LogisticRegression(max_iter=100),
# "Naive Bayes" GaussianNB(),
def predict_top_companys(model, inputs, top_n=3):
    probabilities = model.predict_proba(inputs)
    top_n_indices = (-probabilities).argsort()[:, :top_n]
    top_n_companys = [model.classes_[indices] for indices in top_n_indices]
    return top_n_companys


# Define Streamlit app
def main():

    # Sidebar title and selection
    selected_classifier = st.sidebar.selectbox("Select Classifier", list(models.keys()))

    # Define the columns and their respective names
    columns = {
        "Oracle Cloud Infrastructure Foundations Associate": "oracle_cloud_infrastructure_foundations_associate",
        "AWS Certified Cloud Practitioner": "aws_certified_cloud_practitioner",
        "AWS Certified Solutions Architect - Associate": "aws_certified_solutions_architect_-_associate1",
        "AWS Cloud Practitioner": "aws_cloud_practitioner",
        "MTA Security Fundamentals": "mta_security_fundamentals",
        "MTA Python": "mta_python",
        "Google Cloud Certified Associate Cloud Engineer": "google_cloud_certified_associate_cloud_engineer",
        "MTA Java": "mta_java",
        "Microsoft Azure Fundamentals": "microsoft_azure_fundamentals",
        "Juniper Networks JNCIA-Junos JN0-103 Certified Associate": "junipernetworksjnciajunosjn0103certifiedassociate",
        "MTA 49": "mta49",
        "Thub": "thub",
        "Owl Coder": "owl_coder",
        "Hero Vired": "hero_vired",
        "Both": "both",
        "Photoshop": "photoshop",
        "Unreal Engine": "unreal_engine",
        "React JS": "react_js",
        "Bootstrap": "bootstrap",
        "Cloud": "cloud",
        "Python": "python",
        "JavaScript": "java_script",
        "Express JS": "express_js",
        "C++": "c++",
        "SQL": "sql",
        "Maya": "maya",
        "Blender": "blender",
        "CSS": "css",
        "C#": "c#",
        "C": "c",
    }

    # Create a dictionary to store the values
    values = {}

    # Create sidebar sliders for each column and capture the values
    for display_name, column_name in columns.items():
        if column_name in ["thub", "owl_coder", "hero_vired", "both"]:
            radio_value = st.sidebar.radio(display_name, ["No", "Yes"], index=0)
            values[column_name] = 1 if radio_value == "Yes" else 0
        else:
            slider_value = st.sidebar.slider(
                display_name, min_value=0, max_value=100, value=0
            )
            values[column_name] = slider_value

    # Display captured values
    # st.write("Captured values:", values)
    inputs = [[*values.values()]]
    print(inputs)

    # # Display the array of values
    #     st.write("Array of values:", values_array)

    # if st.sidebar.button("Predict Company"):
    # Perform action when the button is clicked, e.g., call your  function

    # Predict top companies
    if selected_classifier:
        model = models[selected_classifier]
        model.fit(X_train, y_train)
        top_companys = predict_top_companys(model, inputs, top_n=3)

    # Extracting the array of companies from the top_companys variable
    companies_array = top_companys[0]

    st.subheader(f"Most Chances to Get Placed In")

    # Iterate over the companies array and display them as list items
    for i, company in enumerate(companies_array):
        rank = i + 1
        if rank == 2:
            st.header(
                "Other companies with similar skill sets and likelihood of placement"
            )
        st.markdown(
            f"<div style='background-color: orange; padding: 5px; margin-bottom: 5px; font-size: 25px; color: black; font-weight: bold;text-transform: capitalize;'>{rank}. {company}</div>",
            unsafe_allow_html=True,
        )
        # image_path = f'assets/{company}.jpeg'
        # st.image(image_path)
    # Accuracy of predictions
    st.header("Accuracy of Predictions")
    if selected_classifier:
        model = models[selected_classifier]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_train)
        accuracy = accuracy_score(y_train, y_pred) * 100
        st.write(f"The accuracy of {selected_classifier} model is: {accuracy:.2f}")

    # Data exploration
    st.header("Data Exploration")

    # Display dataset
    st.write("### Dataset")
    st.write(df)
    # Histogram for prediction results of classifiers
    st.write("### Histogram for Prediction Results of Classifiers")

    # Prepare data for histograms
    prediction_results = {}
    for classifier_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        prediction_results[classifier_name] = y_pred

    # Create histograms
    for classifier_name, y_pred in prediction_results.items():
        st.subheader(f"Histogram for {classifier_name}")
        plt.figure(figsize=(20, 8))
        sns.histplot(y_pred, bins=len(set(y_pred)), kde=True, color="skyblue")
        plt.xlabel("Predicted Label")
        plt.ylabel("Frequency")
        plt.title(f"Histogram of Prediction Results for {classifier_name}")
        plt.xticks(
            rotation=45, horizontalalignment="right", fontweight="bold", fontsize=8
        )
        st.pyplot()

    # Box Plot
    st.write("### Boxplot for Selected Feature")
    selected_feature = st.selectbox("Select Feature for Boxplot", X.columns)
    plt.figure(figsize=(30, 8))
    sns.boxplot(x="label", y=selected_feature, data=df, palette="Set3")
    plt.xlabel("company Label")
    plt.ylabel(selected_feature)
    plt.title(f"Boxplot of {selected_feature} by company Label")
    plt.xticks(rotation=45, horizontalalignment="right", fontweight="bold", fontsize=8)
    st.pyplot()


if __name__ == "__main__":
    main()
