import os
import json
import re

class OperationData:
    propertyNames = ['date', 'card', 'account', 'accountValidTo', 'client', 'lastName',
                        'firstName', 'patronymic', 'dateOfBirth', 'passport', 'passportValidTo', 'phone', 
                        'operType', 'amount', 'operResult', 'terminal', 'terminalType', 'city', 'address']
    def __init__(self, objectValueList):
        self._rank = 20
        if len(objectValueList) != len(OperationData.propertyNames):
            raise ValueError("Bad data length")
        for i in range(len(objectValueList)):
            value = objectValueList[i]
            if value is not None: 
                key = OperationData.propertyNames[i]
                setattr(self, key, value)
    def toJSON(self):
        return json.dumps(self, default = lambda o: f"{o.__dict__}", indent = 2)
    def set_rank(self, rank):
        self._rank = rank
    def get_rank(self):
        return self._rank
    def __str__(self):
        return "OperationData(%s)" % ','.join([key + ": " + str( getattr(self, key)) for key in OperationData.propertyNames])
    def __repr__(self):
        return str(self)



def readJsonFile(objectsList = []):
    jsonFile = open(f'{os.path.dirname(os.getcwd())}/transactions.json', encoding='utf-8')
    jsonObject = json.load(jsonFile)
    for numberObj, DataObject in enumerate(jsonObject["transactions"]):
        objectValueList = []
        for key in jsonObject["transactions"][DataObject]:
            objectValueList.append(jsonObject["transactions"][DataObject][key])
        objectsList.append(OperationData(objectValueList))
    jsonFile.close()
    return objectsList

def repeatCard(objectsList):
    sameCards = dict()
    for object in objectsList:
        if object.card not in sameCards:
            sameCards.update({object.card: [object]}) 
        else: 
            sameCards[object.card].append(object)
    return sameCards

def outputDictTerminal(dict):
    for key, value in dict.items():
        if(len(value) > 1):
            print( '\n\n', 'Количество повторяющихся операций:', len(value), '\n\n', '----------next-------------')
            for operation in value:
                print('\n')
                for item, val in operation.__dict__.items():
                    print(item, val)

def objToJson(object):
    JSON = json.dumps(object.toJSON())
    JSON = re.sub(r',', lambda o: ',\n', str(object))
    return (JSON + '\r\n')

def globalFilters(objectsList):
    with open('./testFile.txt', 'w+', encoding = 'utf-8') as output:
        for object in objectsList:
            if object.operResult == 'Отказ':
                output.write(objToJson(object))


def __main__():
    objectsList = readJsonFile([])
    globalFilters(objectsList)
    repeatCards = repeatCard(objectsList)
    outputDictTerminal(repeatCards)
        
    

__main__()