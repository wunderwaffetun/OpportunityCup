import os
import json
from typing import List

class OperationData:
    def __init__(self, objectKeyList, objectValueList):
        self.keys = objectKeyList
        self.values = objectValueList
        for i in range(len(key)):
            try: 
                exec("%s = %s" % (self.keys[i], self.values[i]))
            except:
                pass
            
            # self[objectKeyList[i]] = objectValueList[i] 

            
        


jsonFile = open(f'{os.path.dirname(os.getcwd())}/transactions.json', encoding='utf-8')
jsonObject = json.load(jsonFile)
objectsList = list()

for numberObj, DataObject in enumerate(jsonObject["transactions"]):
    objectKeyList = list()
    objectValueList = list()
    for key in jsonObject["transactions"][DataObject]:
        objectKeyList.append(key)
        objectValueList.append(jsonObject["transactions"][DataObject][key])
        # print(key, jsonObject["transactions"][DataObject][key]) 
    objectsList.append(OperationData(objectKeyList, objectValueList))
    break
for key, value in objectsList[0].items():
    print(key, value)



jsonFile.close()