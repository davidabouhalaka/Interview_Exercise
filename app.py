import csv, json
from flask import Flask
import requests

app = Flask(__name__)

csvFilePath = "SREExerciseNames.csv"
jsonFilePath = "SREExerciseNames.json"
# Read the CSV and add the data to a dictionary.

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        fname = csvRow["fname"]
        data[fname] = csvRow
  
        

        

# Write data to a JSON file.
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

with open(jsonFilePath, 'r') as opened_file:
    policy = json.load(opened_file)



@app.route('/')
def hello():
    return data
    
    
@app.route("/search/<name>", methods=['GET'])
def search(name):
    if name in policy:
        return (f'{policy[name]["fname"]} {policy[name]["lname"]} is in the JSON file')
    else:
        return (f"{name} name not found")




        


if __name__ == '__main__':
    app.run()
