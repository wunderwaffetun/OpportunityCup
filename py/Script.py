import os
import json
from typing import List

class OperationData:
    propertyNames = ['values', 'date', 'card', 'account', 'accountValidTo', 'client', 'lastName',
                        'firstName', 'patronymic', 'dateOfBirth', 'passport', 'passportValidTo', 'phone', 
                        'operType', 'amount', 'operResult', 'terminal', 'terminalType', 'city', 'address']
    def __init__(self, objectValueList):
        self.values = objectValueList
        self.date = ''
        self.card = ''
        self.account = ''
        self.accountValidTo = ''
        self.client = ''
        self.lastName = ''
        self.firstName = ''
        self.patronymic = ''
        self.dateOfBirth = ''
        self.passport = ''
        self.passportValidTo = ''
        self.phone = ''
        self.operType = ''
        self.amount = ''
        self.operResult = ''
        self.terminal = ''
        self.terminalType = ''
        self.city = ''
        self.address = ''
    def set_data(self, array):
        if len(array) != len(OperationData.propertyNames):
            raise ValueError("Bad data length")
        for i in range(len(array)):
            value = array[i]
            if value is not None: 
                key = OperationData.propertyNames[i]
                setattr(self, key, value)
    def __str__(self):
        return "OperationData(%s)" % ','.join([str(getattr(self, key)) for key in OperationData.propertyNames])
    def __repr__(self):
        return str(self)

            
        


jsonFile = open(f'{os.path.dirname(os.getcwd())}/transactions.json', encoding='utf-8')
jsonObject = json.load(jsonFile)
objectsList = list()

for numberObj, DataObject in enumerate(jsonObject["transactions"]):
    objectKeyList = list()
    objectValueList = list()
    for key in jsonObject["transactions"][DataObject]:
        objectKeyList.append(key)
        objectValueList.append(jsonObject["transactions"][DataObject][key])
        print(key, jsonObject["transactions"][DataObject][key]) 
    objectsList.append(OperationData(objectValueList))
    break
print(objectsList)





jsonFile.close()