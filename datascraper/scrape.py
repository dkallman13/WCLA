import requests
import json

print("please input your Warcraft logs oauth v2 access token:\n")
tokenID = input()
print("please put which (public) report id you'd like to get \n")
reportID = input()
print("please put which fight id you'd like to get \n")
fightID = input()
fullQuery = (
    """{
    reportData :{
        report: (code: """
    + reportID
    + """ ){
            events(fightIDs:["""
    + fightID
    + """]){
                data
            }
        }
    }
}"""
)

data = requests.get(
    url="https://classic.warcraftlogs.com/api/v2/client",
    data={"query": fullQuery},
    headers={"Authorization": "Bearer " + tokenID},
)
dataParsed = json.loads(data.text)
with open(
    reportID + " " + fightID + ".json", "w", encoding="utf-8"
) as dataFile:
    json.dump(dataParsed, dataFile)
