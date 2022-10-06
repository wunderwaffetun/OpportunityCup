import os
import json
import re
from const import *
from readJSON import *
from dopFunction import *
from Script import *

def globalFilters(objectsList):
    repeatCards = repeatCard(objectsList) #получаем список словарей с уникальными ключами в виде номеров карт
    for object in objectsList:
        if object.get_rank() > 0: #если у нас уже есть в базе фрод, не будем запускать
            impossibleValues(object)
            manyCache(object)
    suspiciouslyDeals(repeatCards)

def impossibleValues(object):
    yearFromPass = int(f"{object.passport}"[2:4]) #выяснили год пасспорта
    if (yearFromPass > nowYear):
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
                # print(object.city, object.date, object.amount, object.terminal[0:3], object.operType, str(timeDifference), isSameOperation)

            if (isToOften and isSameOperation):
                reduceRank(object, penaltyForSameOftenOperation) #вектор не уточнён, требуется доработка, потенциальный фрод, при уточнении, недостаточноть входных данных
            if len(visitedCities) > limitCountVisitedCities:
                reduceRank(object, penaltyForVisetedCities)
            #print('-----------------------next---------------------------')
