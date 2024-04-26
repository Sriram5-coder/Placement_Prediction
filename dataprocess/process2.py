import json
from sklearn.preprocessing import LabelEncoder

with open("data.json", "r") as file:
    data = json.load(file)
for entry in data:
    selected = entry.get("selected", "")
    entry["selected"] = ",".join(
        [category.strip() for category in selected.split(",") if category.strip()]
    )
categories = set()
for entry in data:
    selected = entry.get("selected", "")
    categories.update(selected.split(","))
categories = sorted([category.strip() for category in categories])
label_encoder = LabelEncoder()
label_encoder.fit(categories)
for entry in data:
    selected = entry.get("selected", "")
    labels = label_encoder.transform(
        [category.strip() for category in selected.split(",")]
    )
    entry["category_labels"] = labels.tolist()
with open("labeled_data.json", "w") as file:
    json.dump(data, file, indent=4)
print(
    "Unnecessary commas removed, categories labeled, and data written to labeled_data.json"
)
