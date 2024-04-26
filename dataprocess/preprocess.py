import json
import re

with open("lowercase_data.json", "r") as file:
    data = json.load(file)


def preprocess_data(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_value = preprocess_data(value)
            if key == "selected":
                new_value = [
                    re.sub(r"[^a-zA-Z0-9,]", "", v.strip().lower())
                    for v in new_value.split(",")
                ]
                new_value = [v for v in new_value if v]
            elif key == "certifications" and type(value) is not int:
                new_value = [
                    re.sub(r"[^a-zA-Z0-9,]", "", v.strip().lower())
                    for v in new_value.split(",")
                ]
                new_value = [v for v in new_value if v]
            elif key == "skills":
                new_value = [
                    re.sub(r"[^a-zA-Z0-9,]", "", v.strip().lower())
                    for v in new_value.split(",")
                ]
                new_value = [v for v in new_value if v]
            new_dict[key] = new_value
        return new_dict
    elif isinstance(obj, list):
        new_list = []
        for item in obj:
            new_list.append(preprocess_data(item))
        return new_list
    else:
        return obj


preprocessed_data = preprocess_data(data)

with open("preprocessed_dataset.json", "w") as file:
    json.dump(preprocessed_data, file, indent=2)
