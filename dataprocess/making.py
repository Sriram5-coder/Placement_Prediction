import json

with open("lowercase_data.json", "r") as file:
    data = json.load(file)


def remove_quotes(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_dict[key] = remove_quotes(value)
        return new_dict
    elif isinstance(obj, list):
        new_list = []
        for item in obj:
            new_list.append(remove_quotes(item))
        return new_list
    else:
        if isinstance(obj, str):
            try:
                return int(obj)
            except ValueError:
                try:
                    return float(obj)
                except ValueError:
                    return obj.replace("'", "")
        else:
            return obj


new_data = remove_quotes(data)
with open("new_dataset.json", "w") as file:
    json.dump(new_data, file, indent=2)
