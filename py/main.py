from config import *
from generalFunctions import *
from readJSON import *
from additionalFunctions import *
from exportData import *

def globalFilters(objectsList):
    
    repeatCards = repeatCard(objectsList) #получаем список словарей с уникальными ключами в виде номеров карт
    repeatPassports = repeatPassport(objectsList)
    for object in objectsList:
        if object.get_rank() > 0: #если у нас уже есть в базе фрод, не будем запускать
            impossibleValueYearFromPas(object)
            frodRrefillPOS(object)
            frodNightTime(object)
            frodValidTo(object)
            manyCache(object)
    suspiciouslyDeals(repeatCards)
    listOfPassManyOperrations = manyOperationsByOnePass(repeatPassports)
    reduceForManyPassportsOperations(objectsList, listOfPassManyOperrations)
    checkCorreckDataObject(objectsList, repeatCards)
    exportToFile(objectsList)
    for object in objectsList:
        if(len(object.get_incorrect_data())>0):
            print(object.get_incorrect_data(), object.get_rank(), object.card, "main.py")
    

if __name__ == '__main__':
    objectsList = readJsonFile([])  #получаем список json объектов
    changeObjDates(objectsList) #заменяем строковые даты на объекты дат
    globalFilters(objectsList) #основная фильтрующая функция
    
