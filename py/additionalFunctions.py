from config import *
from generalFunctions import *
from readJSON import *
from main import *

def repeatCard(objectsList):
    sameCards = dict()
    for object in objectsList:
        if object.card not in sameCards:
            sameCards.update({object.card: [object]})
        else:
            sameCards[object.card].append(object)
    return sameCards

def findAndReduceByParametr(objectsList, **kwargs): #чисто для фрода, можно поправить уменьшаемое значение (4 пункт)
    #findAndReduceByParametr(objectsList, card = "56037470176508885939", client = "8-44184") #проверка 4 пункта
    for key in kwargs.keys(): #пришли ли данные, которых нет в классе: object.akjfdd
        if key not in objectsList[0].get_properties_name():
            raise ValueError("There are no such parametr or parametrs P.S. findAndReduceByParametr()")
    for prop, value in kwargs.items():
        for object in objectsList:
            if getattr(object, prop) == value:
                # object.set_rank(0)
                reduceRank(object, penaltyForPasError)

def outputDictTerminal(dict):
    for key, value in dict.items():
        if(len(value) >= 1):
            print( '\n\n', '----------next-------------', '\n\n', 'Количество повторяющихся операций:', len(value))
            for operation in value:
                print('\n')
                for item, val in operation.__dict__.items():
                    print(item, val)



def definePattern(currentFraudPattern, object):
    currentFraudPattern = currentFraudPattern.strip()
    if(currentFraudPattern):
        object.set_fraud_patterns(currentFraudPattern)

def incorrectData(currentIncorrectData, object):
    currentIncorrectData = currentIncorrectData.strip()
    if(currentIncorrectData):
        object.set_incorrect_data(currentIncorrectData)

def findAndReduceByParametr(objectsList, **kwargs): #чисто для фрода, можно поправить уменьшаемое значение (4 пункт)
    #findAndReduceByParametr(objectsList, card = "56037470176508885939", client = "8-44184") #проверка 4 пункта
    for key in kwargs.keys():
        if key not in objectsList[0].get_properties_name():
            raise ValueError("There are no such parametr or parametrs P.S. findAndReduceByParametr()")
    for object in objectsList:
        for property, value in kwargs.items():
            if getattr(object, property) == value:
                reduceRank(object, 30)

def reduceRank(object, quantity): #универсальная функция, уменьшающая приоритетность операции
    #Здесь мы смотрим на operResult, это нужно, чтобы, например, если человек забыл, что просрочился
    #аккаунт, его рейтинг не улетал в 0, однако если он пытается это делать постоянно, постепенно рейтинг снижается
    if(object.operResult != "Отказ"):
        object.set_rank(object.get_rank() - quantity)
    else:
        object.set_rank(object.get_rank() - penaltyForRejectionAndFrod)
    if object.get_rank() < 0:
        object.set_rank(0)
def strToTime(strTime): #универсальная функция, переводит строку во время
    return datetime.datetime.strptime(strTime, "%H:%M:%S").time()

def tryExceptDecorator(handlingDataTime): #дописать декоратор для changeObjDates()
    try:
        return datetime.datetime.strptime(handlingDataTime, "%Y-%m-%dT%H:%M:%S")
    except:
        return datetime.datetime.strptime(handlingDataTime, "%Y-%m-%d")

def changeObjDates(list): #нужна для переопределения строк в объекте на объект даты
    for object in list:
        object.date = datetime.datetime.strptime(object.date, "%Y-%m-%dT%H:%M:%S")
        object.passportValidTo = tryExceptDecorator(object.passportValidTo)
        object.dateOfBirth = tryExceptDecorator(object.dateOfBirth)
        object.accountValidTo = tryExceptDecorator(object.accountValidTo)
