from config import *
from readJSON import *
from additionalFunctions import *
from main import *
from frodForPas import *

def findAndReduceByParametr(objectsList, **kwargs): #чисто для фрода, можно поправить уменьшаемое значение (4 пункт)
    #findAndReduceByParametr(objectsList, card = "56037470176508885939", client = "8-44184") #проверка 4 пункта
    for key in kwargs.keys(): #пришли ли данные, которых нет в классе: object.akjfdd
        if key not in objectsList[0].get_properties_name():
            raise ValueError("There are no such parametr or parametrs P.S. findAndReduceByParametr()")
    for prop, value in kwargs.items():
        for object in objectsList:
            if getattr(object, prop) == value:
                object.set_rank(0)

def checkCorreckDataObject(objectsList, repeatCards): #1 пункт
    for numberCard in repeatCards.keys():
        if len(repeatCards[numberCard]) > 1:
            obj = repeatCards[numberCard][0]
            passport = obj.passport
            fio = f"{obj.lastName}{obj.firstName}{obj.patronymic}"
            passportValidTo = obj.passportValidTo
            accountValidTo = obj.accountValidTo
            account = obj.account
            client = obj.client
            birth = obj.dateOfBirth
            listOfParametrs = [passport, fio, passportValidTo, accountValidTo, account, client, birth]
            for i in range(len(repeatCards[numberCard])):
                object = repeatCards[numberCard][i]
                listOfCurrentParametrs = [object.passport, f"{object.lastName}{object.firstName}{object.patronymic}",
                                            object.passportValidTo, object.accountValidTo, object.account,
                                            object.client, object.dateOfBirth]
                if listOfCurrentParametrs != listOfParametrs:
                    findAndReduceByParametr(objectsList, card = object.card, passport = object.passport, lastName = object.lastName,
                                            firstName = object.firstName, patronymic = object.patronymic,
                                            passportValidTo = object.passportValidTo, accountValidTo = object.accountValidTo,
                                            account = object.account, client = object.client, dateOfBirth = object.dateOfBirth)
def impossibleValues(object):
    yearFromPass = int(f"{object.passport}"[2:4]) #выяснили год пасспорта
    if (yearFromPass > NextYear):
        yearFromPass = int("19"+f"{object.passport}"[2:4])
    else:
        yearFromPass = int("20"+f"{object.passport}"[2:4])
    terminal = object.terminal[0:3]
    ageClient = object.date.year - object.dateOfBirth.year #реальный возраст клиента на момент итерации с банком
    ageCalculateFromPas = yearFromPass - object.dateOfBirth.year #возраст клиента на момент получения паспорта
    if(terminal == "POS" and object.operType == "Пополнение"):#пополнение через POS
        reduceRank(object, penaltyForRefillPOS)

    if(((object.date.time() >= strToTime("22:00:00")) and #ночное время
        (object.date.time() <= strToTime("23:59:59"))) or
        ((object.date.time() >= strToTime("00:00:00")) and
        (object.date.time() <= strToTime("06:00:00")))):
        reduceRank(object, penaltyForRefillPOS)

    if(yearFromPass < limitMinYearPas or
        yearFromPass > limitMaxYearPas or                          # несуществующая серия паспорта
        ageClient < limitMinAgeForPas or                                    # ранняя выдача паспорта
        ageCalculateFromPas < (limitMinAgeForPas - deltaSiriesInYearIssuance) or                          # слишком молод для своей серии
        ageClient > limitMaxAge):
        reduceRank(object, penaltyForPasError)

    if (object.date > object.accountValidTo or object.date > object.passportValidTo):
        reduceRank(object, penaltyForValidTo)

def manyCache(object):
    if(object.operType == 'Снятие' and object.terminal[0:3] == "ATM" and object.amount > limitWithdrawalATM): # если снимаем много налички
        reduceRank(object, penaltyForWithdrawalATM)

def suspiciouslyDeals(repeatCards): # 3 и более смены мест + промежутки между снятиями небольшие
    for numberCard in repeatCards.keys():
        if len(repeatCards[numberCard]) > 1:
            isToOften = False
            isSameOperation = False
            visitedCities = set()
            threeChangingCity = False
            startTime = repeatCards[numberCard][0].date
            firstOpperation = repeatCards[numberCard][0].operType
            for i in range(len(repeatCards[numberCard])):
                object = repeatCards[numberCard][i]
                visitedCities.add(object.city)
                if i != 0:
                    timeDifference = object.date - startTime
                    if timeDifference.total_seconds() < timeDelta.total_seconds(): isToOften = True
                    if firstOpperation == object.operType: isSameOperation = True
                else: timeDifference = None
            if (isToOften and isSameOperation):
                reduceRank(object, penaltyForSameOftenOperationCart) #вектор не уточнён, требуется доработка, потенциальный фрод, при уточнении, недостаточноть входных данных
            if len(visitedCities) > limitCountVisitedCities:
                reduceRank(object, penaltyForVisetedCities)
