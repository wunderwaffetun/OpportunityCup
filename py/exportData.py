import os
from config import *
from filtersFunctions import *
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
            exportData.write(f"{object.get_number()}\n")
    exportData.write(f"{count} - всего")
    exportData.close()
