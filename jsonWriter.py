import json
### IMPORTING REPOSITORIES


### DATA TO BE WRITTEN IN THE JSON FILE
dictionary={
    'name':"Ali",
    'Age':"21",
    'Birth date':"10.06.2003",
    "Favourite color":"Green"
}



# SERIALIZING JSON

json_object=json.dumps(dictionary,indent=4)


# WRITING THE DATA TO sample.json 

with open("sample.json","w") as outfile:
    outfile.write(json_object)

