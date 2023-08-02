import requests
import json

print("please input your Warcraft logs oauth v2 access token:\n")
tokenID = input()
print("please put which (public) report id you'd like to get \n")
reportID = input()
print("please put which fight id you'd like to get first \n")
firstFightID = input()
print("please put which fight id you'd like to get last \n")
lastFightID = input()
if int(firstFightID) < 1 | int(lastFightID) < 1:
    print("the first or last fight has to be a whole number greater than 0")
elif (int(firstFightID) > int(lastFightID)):
    print("the first has to be less than or equal to the second number")
else:
    for i in range(int(firstFightID), int(lastFightID)+1):
        fullQuery = (
            """query{
        reportData{
            report(code: \""""
            + reportID
            + """ \"){
                events(fightIDs:["""
            + str(i)
            + """]){
                    data
                }
            }
        }
    }"""
        )
        data = requests.get(
            url="https://classic.warcraftlogs.com/api/v2/client",
            params={"query": fullQuery},
            headers={"Authorization": "Bearer " + tokenID},
        )
        dataParsed = json.loads(data.text)
        with open("./data/" + reportID + " " + str(i) + ".json", "w", encoding="utf-8") as dataFile:
            json.dump(dataParsed, dataFile)
