from config import *
from config import firstStartFunctionDeals
from readJSON import *
from additionalFunctions import *
from main import *


def checkCorreckDataObjects(objectsList, repeatParametrs, listCheckAttributes): #1 пункт
    for numberParametr in repeatParametrs.keys():
        if len(repeatParametrs[numberParametr]) > quantityOperationsByOneCardOrPass:
            obj = repeatParametrs[numberParametr][0]
            listOfParametrs = [getattr(obj, par) for par in listCheckAttributes]
            for i in range(len(repeatParametrs[numberParametr])):
                object = repeatParametrs[numberParametr][i]
                listOfCurrentParametrs = [getattr(object, param) for param in listCheckAttributes]
                if listOfCurrentParametrs != listOfParametrs:
                    incorrectData("DIFFERENT_DATA", object)
                    findAndReduceByParametr(objectsList, card = object.card, passport = object.passport)


def impossibleValueYearFromPas(object):#проверка корректности серрии паспорта и возраста клиента
    yearFromPass = int(f"{object.passport}"[2:4]) #выяснили год пасспорта
    if (yearFromPass > NextYear):
        yearFromPass = int("19"+f"{object.passport}"[2:4])
    else:
        yearFromPass = int("20"+f"{object.passport}"[2:4])
    ageClient = object.date.year - object.dateOfBirth.year  # реальный возраст клиента на момент итерации с банком
    ageCalculateFromPas = yearFromPass - object.dateOfBirth.year  # возраст клиента на момент получения паспорта
    if(yearFromPass < limitMinYearPas or
        yearFromPass > limitMaxYearPas or                          # несуществующая серия паспорта
        ageClient < limitMinAgeForPas or                                    # ранняя выдача паспорта
        ageCalculateFromPas < (limitMinAgeForPas - deltaSiriesInYearIssuance) or                          # слишком молод для своей серии
        ageClient > limitMaxAge):
        incorrectData("INCORRECT_CLIENT_AGE", object)
        reduceRank(object, penaltyForPasError)


def frodRrefillPOS (object):
    terminal = object.terminal[0:3]
    if(terminal == "POS" and object.operType == "Пополнение"):#пополнение через POS
        reduceRank(object, penaltyForRefillPOS)
        definePattern('POS_TERMINAL', object)

def frodNightTime (object):
    if(((object.date.time() >= strToTime("22:00:00")) and #ночное время
        (object.date.time() <= strToTime("23:59:59"))) or
        ((object.date.time() >= strToTime("00:00:00")) and
        (object.date.time() <= strToTime("06:00:00")))):
        reduceRank(object, penaltyForNightTime)
        definePattern('NIGHT_TIME', object)

def frodValidTo (object):
    if (object.date > object.accountValidTo or object.date > object.passportValidTo):
        definePattern('PASSPORT_OR_ACCOUNT_NO_VALID', object)
        reduceRank(object, penaltyForValidTo)

def manyCache(object):
    if(object.operType == 'Снятие' and object.terminal[0:3] == "ATM" and object.amount > limitWithdrawalATM): # если снимаем много налички
        reduceRank(object, penaltyForWithdrawalATM)
        definePattern('CASH_OUT_ATM_TERMINAL', object)

def suspiciouslyDeals(repeatParametrs): # 3 и более смены мест + промежутки между снятиями небольшие
    global firstStartFunctionDeals
    for numberParametr in repeatParametrs.keys():
        if len(repeatParametrs[numberParametr]) > 1:
            isToOften = False
            isSameOperation = not includeSameOperations
            visitedCities = set()
            startTime = repeatParametrs[numberParametr][0].date
            firstOpperation = repeatParametrs[numberParametr][0].operType
            for i in range(len(repeatParametrs[numberParametr])):
                object = repeatParametrs[numberParametr][i]
                visitedCities.add(object.city)
                if i != 0:
                    timeDifference = object.date - startTime
                    if timeDifference.total_seconds() < timeDelta.total_seconds(): isToOften = True
                    if firstOpperation == object.operType: isSameOperation = True
                else: timeDifference = None
            if (isToOften and isSameOperation):
                reduceRank(object, penaltyForSameOftenOperationCart) #вектор не уточнён, требуется доработка, потенциальный фрод, при уточнении, недостаточноть входных данных
                definePattern('OFTEN_SAME_OPERATIONS', object)
            if (len(visitedCities) > limitCountVisitedCities) and firstStartFunctionDeals: 
                reduceRank(object, penaltyForVisetedCities)
                definePattern('OFTEN_CHANGE_CITY', object)
    firstStartFunctionDeals = False