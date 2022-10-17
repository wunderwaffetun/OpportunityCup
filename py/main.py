from config import *
from generalFunctions import *
from readJSON import *
from additionalFunctions import *
from exportData import *

def globalFilters(objectsList):
    repeatCards = createRepeatDictByKey(objectsList, 'card') #получаем список словарей с уникальными ключами в виде номеров карт
    repeatPassports = createRepeatDictByKey(objectsList, 'passport')
    repeatAccounts = createRepeatDictByKey(objectsList, 'account')
    for object in objectsList:
        if object.get_rank() > 0: #если у нас уже есть в базе фрод, не будем запускать
            impossibleValueYearFromPas(object)
            FraudRrefillPOS(object)
            FraudNightTime(object)
            FraudValidTo(object)
            manyCache(object)
    suspiciouslyDeals(repeatCards) #всё равно 0 совпадений 
    suspiciouslyDeals(repeatPassports)
    suspiciouslyDeals(repeatAccounts) #всё равно 0 совпадений
    checkCorreckDataObjects(objectsList, repeatPassports, ['passport', 'lastName', 'firstName', 'patronymic', 
                                'passportValidTo', 'accountValidTo', 'account', 'client', 'dateOfBirth']) #Нужно сделать проверку на дату совершения
    checkCorreckDataObjects(objectsList, repeatAccounts, ['passport'])


    exportToFile(objectsList)
    # for object in objectsList:
        # if(len(object.get_incorrect_data())>=0):
        # if(len(object.get_fraud_patterns())>0):
            # print(object.get_incorrect_data(), object.get_rank(), object.card, "main.py")
            # print(object.get_fraud_patterns(), object.get_rank(), object.card, "main.py")
    

if __name__ == '__main__':
    startTime = datetime.datetime.now()
    objectsList = readJsonFile([])  #получаем список json объектов
    changeObjDates(objectsList) #заменяем строковые даты на объекты дат
    globalFilters(objectsList) #основная фильтрующая функция
    print('Отработало за', (datetime.datetime.now() - startTime).total_seconds(), 'секунд')
