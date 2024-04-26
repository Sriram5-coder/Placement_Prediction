import json

with open("data.json", "r") as file:
    json_data = file.read()
data = json.loads(json_data)


def lowercase_strings(obj):
    if isinstance(obj, str):
        return obj.lower()
    elif isinstance(obj, list):
        return [lowercase_strings(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: lowercase_strings(value) for key, value in obj.items()}
    else:
        return obj


lowercase_data = lowercase_strings(data)
with open("lowercase.json", "w") as file:
    json.dump(lowercase_data, file, indent=4)
print("Lowercase data has been written to lowercase_data.json")
