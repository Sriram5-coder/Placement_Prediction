import json

with open("dataset.json", "r") as file:
    data = json.load(file)
for entry in data:
    del entry["studentid"]
    del entry["roll"]
    del entry["studentname"]
    del entry["package"]
with open("modified_data.json", "w") as file:
    json.dump(data, file, indent=4)
print("Fields removed and modified data written to modified_data.json")
