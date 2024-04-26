import pandas as pd
from joblib import load

# Load the saved MultiOutputClassifier model
classifier = load("random_forest_model.joblib")

def predict_labels_for_new_data(new_data_point):
    # Define default values for missing features
    default_values = {
        'oracle_cloud_infrastructure_foundations_associate': 0,
        'aws_certified_cloud_practitioner': 0,
        'aws_certified_solutions_architect_-_associate1': 0,
        'aws_cloud_practitioner': 0,
        'mta_security_fundamentals': 0,
        'mta_python': 0,
        'google_cloud_certified_associate_cloud_engineer': 0,
        'mta_java': 0,
        'microsoft_azure_fundamentals': 0,
        'junipernetworksjnciajunosjn0103certifiedassociate': 0,
        'mta49': 0,
        'thub': 0,
        'owl_coder': 0,
        'hero_vired': 0,
        'both': 0,
        'photoshop': 0,
        'unreal_engine': 0,
        'react_js': 0,
        'bootstrap': 0,
        'cloud': 0,
        'python': 0,
        'java_script': 0,
        'express_js': 0,
        'c++': 0,
        'sql': 0,
        'maya': 0,
        'blender': 0,
        'css': 0,
        'c#': 0,
        'c': 0
    }

    # Update new_data_point with default values for missing keys
    updated_new_data_point = {**default_values, **new_data_point}

    # Convert the new data to DataFrame format
    new_data_df = pd.DataFrame([updated_new_data_point])

    # Predict using the trained classifier
    predicted_labels = classifier.predict(new_data_df)

    return predicted_labels[0]

# Example usage:
new_data_point = {
    'aws_certified_cloud_practitioner': 1,
    'mta_python': 1,
    'photoshop': 1,
    'unreal_engine': 1,
    'java_script': 1,
    'c#' : 1
}

predicted_label = predict_labels_for_new_data(new_data_point)
print("Predicted Label:", predicted_label)
