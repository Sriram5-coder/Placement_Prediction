selected = {
    "tcs digital": 1,
    "vihaan electrix": 2,
    "node js": 3,
    "mongo db": 4,
    "machine learning": 5,
    "palle technologies": 6,
    "value momentum": 7,
    "jio": 8,
    "tech mahindra": 9,
    "zenq": 10,
    "yamaha motor electronics": 11,
    "hexaware": 12,
    "the tech destiny": 13,
    "go digit general": 14,
    "zf india": 15,
    "atkins": 16,
    "kyndryl": 17,
    "tyke": 18,
    "mta java": 19,
    "dxc": 20,
    "kenpath technologies pvt. ltd": 21,
    "surya tech": 22,
    "qspiders": 23,
    "cohance": 24,
    "hyundai steel": 25,
    "vidal": 26,
    "mahindra": 27,
    "tcs ninja": 28,
    "kiml": 29,
    "delphi tvs": 30,
    "larsen & toubro": 31,
    "bscpl": 32,
    "sri scl infratech": 33,
    "pentagon space": 34,
    "besten engineers & consultants": 35,
    "techwave": 36,
    "ramky": 37,
    "sdvvl": 38,
    "lekha": 39,
    "ren labs": 40,
    "bharath group": 41,
    "quest global": 42,
    "symphony retailai": 43,
    "kj systems,apt online": 44,
    "deloitte usi": 45,
    "invi": 46,
    "park controls & communications": 47,
    "figma": 48,
    "html": 49,
    "aparna": 50,
    "keka": 51,
    "extramarks": 52,
    "moveinsync": 53,
    "zemoso": 54,
    "nsl": 55,
    "cartrade tech": 56,
    "java": 57,
    "kj systems": 58,
    "adp": 59,
    "maersk": 60,
    "magikminds": 61,
    "ibm": 62,
    "altcognito": 63,
    "unschool": 64,
    "ball beverage packaging (india) pvt ltd": 65,
    "aws": 66,
    "certified solutions architect - associate": 67,
    "zopsmart": 68,
    "hitachi vantara": 69,
    "thoughtclan": 70,
    "hexaview": 71,
    "cdk global": 72,
    "yubi": 73,
    "nxt wave": 74,
}

certifications = {
    "oracle cloud infrastructure foundations associate": 1,
    "aws certified cloud practitioner": 2,
    "aws certified solutions architect - associate1": 3,
    "aws cloud practitioner": 4,
    "mta security fundamentals": 5,
    "mta python": 6,
    "google cloud certified associate cloud engineer": 7,
    "mta java": 8,
    "microsoft azure fundamentals": 9,
}

thubornot = {"thub": 1, "None": 0}

owlhero = {"None": 0, "owl coder": 1, "hero vired": 2}

skills = {
    "photoshop": 1,
    "unreal engine": 2,
    "react js": 3,
    "bootstrap": 4,
    "cloud": 5,
    "python": 6,
    "java script": 7,
    "express js": 8,
    "c++": 9,
    "sql": 10,
    "maya": 11,
    "blender": 12,
    "css": 13,
    "c#": 14,
}

import json

# Load the JSON data
with open("lowercase.json", "r") as file:
    data = json.load(file)


def replace_labels(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_value = replace_labels(value)
            if key == "selected":
                new_value = [
                    replace_value(v.strip(), selected) for v in new_value.split(",")
                ]
            elif key == "certifications":
                new_value = [
                    replace_value(v.strip(), certifications)
                    for v in new_value.split(",")
                ]
            elif key == "skills":
                new_value = [
                    replace_value(v.strip(), skills) for v in new_value.split(",")
                ]
            elif key == "thubornot":
                new_value = replace_value(str(new_value), thubornot)
            elif key == "owlhero":
                new_value = replace_value(str(new_value), owlhero)
            new_dict[key] = new_value
        return new_dict
    elif isinstance(obj, list):
        new_list = []
        for item in obj:
            new_list.append(replace_labels(item))
        return new_list
    else:
        return obj


def replace_value(value, dictionary):
    if value in dictionary:
        return dictionary[value]
    else:
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value


# Replace labels in the data
new_data = replace_labels(data)

# Save the modified data to a new JSON file
with open("2new_dataset.json", "w") as file:
    json.dump(new_data, file, indent=2)
