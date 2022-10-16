import os
from config import *
from generalFunctions import *
from readJSON import *
from additionalFunctions import *
from exportData import *
from Sheet import *


def exportToFile(objectsList):
    count = 0
    exportData = open(f'{os.path.dirname(os.getcwd())}/py/exportData.txt', 'w+', encoding='utf-8')
    exportData.seek(0)
    frodObjects=[[]]
    for object in objectsList:
        if(object.get_rank() < fraudOperationValue):
            count += 1
            exportData.write(f"{object.get_number()} {object.get_fraud_patterns() if object.get_fraud_patterns() != set() else 'Нет паттернов'} {object.get_incorrect_data() if object.get_incorrect_data() != set() else 'Нет ошибок'} {object.get_rank()}\n")
            frodObjects.append([object.get_number()])
            # # exportData.write(f"{object.fraudPatterns}")
            # rangeObj = 'TestList!A' + str(count + 1) + ':A' + str(count + 1)
            # valuesObj = [[object.get_number()]]
            # importToSheet(rangeObj, valuesObj)
    exportData.write(f"{count} - всего")
    exportData.close()    
    # print(frodObjects)

    valuesCount = [ [ "count:", count]]
    importToSheet('TestList!A1:B2', valuesCount)
    
    importToSheet('TestList!A3:A3', [["FrodNumber"]])
    rangeObjects = 'TestList!A3:A' + str(len(frodObjects) + 2)
    valuesObjects = frodObjects
    importToSheet(rangeObjects, valuesObjects)

