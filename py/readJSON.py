import os
import json
import re
from config import *
from main import *
from generalFunctions import *
from additionalFunctions import *

class OperationData:
    propertyNames = ['date', 'card', 'account', 'accountValidTo', 'client', 'lastName',
                        'firstName', 'patronymic', 'dateOfBirth', 'passport', 'passportValidTo', 'phone',
                        'operType', 'amount', 'operResult', 'terminal', 'terminalType', 'city', 'address']
    fraudPatterns = set()
    def __init__(self, objectValueList, number):
        self._numberOperation = number
        self._rank = rank
        if len(objectValueList) != len(OperationData.propertyNames):
            raise ValueError("Bad data length")
        for i in range(len(objectValueList)):
            value = objectValueList[i]
            if value is not None:
                key = OperationData.propertyNames[i]
                setattr(self, key, value)
    def get_number(self):
        return self._numberOperation
    def set_fraud_patterns(self, pattern):
        self.fraudPatterns.add(pattern)
    def toJSON(self):
        return json.dumps(self, default = lambda o: f"{o.__dict__}", indent = 2)
    def set_rank(self, rank):
        self._rank = rank
    def get_properties_name(self):
        return self.propertyNames
    def get_rank(self):
        return self._rank
    def __str__(self):
        return "OperationData(%s)" % ','.join([key + ": " + str( getattr(self, key)) for key in OperationData.propertyNames])
    def __repr__(self):
        return str(self)

def readJsonFile(objectsList = []):
    jsonFile = open(f'{os.path.dirname(os.getcwd())}/transactions_final.json', encoding='utf-8')
    jsonObject = json.load(jsonFile)
    for numberObj, DataObject in enumerate(jsonObject["transactions"]):
        objectValueList = []
        for key in jsonObject["transactions"][DataObject]:
            objectValueList.append(jsonObject["transactions"][DataObject][key])
        objectsList.append(OperationData(objectValueList, DataObject))
    jsonFile.close()
    return objectsList

def objToJson(object):
    JSON = json.dumps(object.toJSON())
    JSON = re.sub(r',', lambda o: ',\n', str(object))
    return (JSON + '\r\n')