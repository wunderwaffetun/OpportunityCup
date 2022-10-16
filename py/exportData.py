import os
from config import *
from generalFunctions import *
from readJSON import *
from additionalFunctions import *
from exportData import *


def exportToFile(objectsList):
    count = 0
    exportData = open(f'{os.path.dirname(os.getcwd())}/py/exportData.txt', 'w+', encoding='utf-8')
    exportData.seek(0)
    for object in objectsList:
        if(object.get_rank() < fraudOperationValue):
            count += 1
            exportData.write(f"{object.get_number()} {object.get_fraud_patterns() if object.get_fraud_patterns() != set() else 'Нет паттернов'} {object.get_incorrect_data() if object.get_incorrect_data() != set() else 'Нет ошибок'} {object.get_rank()}\n")
            # exportData.write(f"{object.fraudPatterns}")
    exportData.write(f"{count} - всего")
    exportData.close()
