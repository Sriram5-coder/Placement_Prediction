import mysql.connector
import pandas as pd
# Establish connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost", user="test", password="test", database="test"
)
df = pd.read_json("datasetfile.json")
cursor = connection.cursor()

# Define dictionaries
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
    "musigma": 75,
    "legato": 76,
    "46ai": 77,
    "apxor": 78,
    "divami": 79,
    "infor": 80,
    "iquadra": 81,
    "vit": 82,
    "faceprep": 83,
    "digitaltrust": 84,
    "embeautomations": 85,
    "turbohire": 86,
    "acuvate": 87,
    "netmeds": 88,
    "schlumberger": 89,
    "tessolve": 90,
    "appsassociates": 91,
    "jmangroup": 92,
    "tejasnetworks": 93,
    "evertzindia": 94,
    "smsinfrastructure": 95,
    "indiacements": 96,
    "ltecc": 97,
    "nisargaits": 98,
    "techarionpvtltd": 99,
    "celebaltechnology": 100,
    "byjus": 101,
    "cognizant": 102,
    "tapplent": 103,
    "vintrus": 104,
    "acmegrade": 105,
    "cdk": 106,
    "kodnest": 107,
    "efftronics": 108,
    "softsuave": 109,
    "mayinkrishventurespvtltd": 110,
    "myracle": 111,
    "mountblue": 112,
    "aimlds": 113,
    "deevyashaktiindia": 114,
    "12pget": 115,
    "nineleaps": 116,
    "lendenclub": 117,
    "northernarc": 118,
    "exoticlearningnirvodaypvtltd": 119,
    "autocracymachinery": 120,
    "ranemadras": 121,
    "hyundaimotor": 122,
    "ballcorporation": 123,
    "lowes": 124,
    "veefin": 125,
    "deltax": 126,
    "josh": 127,
    "netenrich": 128,
    "aptonline": 129,
    "abb": 130,
    "amazon": 131,
    "alohatechnology": 132,
    "nccltd": 133,
    "ashvaallterrain": 134,
    "epirocminingindia": 135,
    "inscriptaai": 136,
    "mearsk": 137,
    "accenture": 138,
    "technicalhub": 139,
    "sidsfarm": 140,
    "aloha": 141,
    "hp": 142,
    "tcs": 143,
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
    "junipernetworksjnciajunosjn0103certifiedassociate": 10,
    "mta49": 11,
}

thubornot = {"thub": 1}

owlhero = {"owl coder": 1, "hero vired": 2, "both": 3}

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
    "c": 15,
}

# Function to replace spaces with underscores in keys of a dictionary
def replace_spaces_with_underscores(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_key = key.replace(" ", "_")
        new_dict[new_key] = value
    return new_dict

# Replace spaces with underscores in the selected dictionary
selected = replace_spaces_with_underscores(selected)

# Replace spaces with underscores in the certifications dictionary
certifications = replace_spaces_with_underscores(certifications)

# Testing the result
skills = replace_spaces_with_underscores(skills)
owlhero = replace_spaces_with_underscores(owlhero)
thubornot = replace_spaces_with_underscores(thubornot)
# print(selected)
# print(certifications)
# print(owlhero)
# print(skills)

# create_table_query = "CREATE TABLE IF NOT EXISTS sairam (selected VARCHAR(50), "
# for label_dict in [certifications, thubornot, owlhero, skills]:
#     for key in label_dict.keys():
#         create_table_query += "`{}` INT, ".format(key)
# create_table_query = create_table_query[:-2] + ")"  # Remove the trailing comma and space, then add closing bracket
# cursor.execute(create_table_query)




import time

company = df["selected"]

# for i in company:
#     print(i)
#     for j in i:
#         print(j)
#         if j > 143:
#             time.sleep(5)
#             print("hello"*230)
            

def get_key(label, val):

    for key, value in label.items():
        if val == value:
            return key

    return "key doesn't exist"


# Function to split numbers greater than 11 into their individual digits
def split_numbers(num, lessthan):
    if num > lessthan:
        return [int(digit) for digit in str(num)]
    else:
        return [num]


for i in range(1413):
    eachcom = df["selected"][i]
    print("Each company : ", eachcom)
    
    # lst = ",".join(str(x) for x in eachcom)
    # lst = f"({lst})"
    # getdata = f"SELECT * FROM companyplaced where company_id in {lst}"
    # print("My sql query data : ", getdata)
    # # Execute the SQL query
    # cursor.execute(getdata)
    # result = cursor.fetchall()
    # for row in result:
    #     print("Get each row using id : ", row)
    print("__" * 20)
    for start in eachcom:
        
        getcompany = get_key(selected,start)
        print("Name : ",getcompany)
        companyname = start
        print("Company Name : ", companyname)

        insets = f"insert into sairam (selected,company_id) values ('{getcompany}',{i+1})"
        cursor.execute(insets)
        getskills = df["skills"][i]
        getskills = [split_numbers(num, 15) for num in getskills]
        getskills = [item for sublist in getskills for item in sublist]
        print("skills : ", getskills)

        getcertifications = df["certifications"][i]
        getcertifications = [split_numbers(num, 11) for num in getcertifications]
        getcertifications = [item for sublist in getcertifications for item in sublist]
        print("Certifications : ",getcertifications)

        getthubornot = df["thubornot"][i]
        print(getthubornot)
        # getthubornot = [split_numbers(num,15) for num in getthubornot]
        # getthubornot = [item for sublist in getthubornot for item in sublist]

        getowlhero = df["owlhero"][i]
        print(getowlhero)
        # getowlhero = [split_numbers(num,15) for num in getowlhero]
        # getowlhero = [item for sublist in getowlhero for item in sublist]

        for labelname in getskills:
            print("labelname : ", labelname)
            getkey = get_key(skills, labelname)
            print(getkey)
            update_query = f"UPDATE sairam SET `{getkey}` = 1 WHERE selected = '{getcompany}' and company_id = {i+1}"
            print(update_query)
            cursor.execute(update_query)

        if isinstance(getcertifications, list):
            for labelname in getcertifications:
                print("labelname : ", labelname)
                getkey = get_key(certifications, labelname)
                print(getkey)
                if labelname > 0:
                    update_query = f"UPDATE sairam SET `{getkey}` = 1 WHERE selected = '{getcompany}' and company_id = {i+1}"
                    print(update_query)
                    cursor.execute(update_query)

        if getthubornot == 1:
            for labelname in range(1, getthubornot + 1):
                print("labelname : ", labelname)
                getkey = get_key(thubornot, labelname)
                print(getkey)
                update_query = f"UPDATE sairam SET `{getkey}` = 1 WHERE selected = '{getcompany}' and company_id = {i+1}"
                print(update_query)
                cursor.execute(update_query)

        if getowlhero >= 1:
            for labelname in range(1, getowlhero + 1):
                print("labelname : ", labelname)
                getkey = get_key(owlhero, labelname)
                print(getkey)
                if labelname > 0:
                    update_query = f"UPDATE sairam SET `{getkey}` = 1 WHERE selected = '{getcompany}' and company_id = {i+1}"
                    print(update_query)
                    cursor.execute(update_query)






# Commit the changes and close the connection
connection.commit()
connection.close()