import os
import json
import re
from const import *
from filtersFunc import *
from readJSON import *
from dopFunction import *
from Script import *

def repeatPassport(objectsList):
    samePassports = dict()
    for object in objectsList:
        if object.passport not in samePassports:
            samePassports.update({object.passport: [object]})
        else:
            samePassports[object.passport].append(object)
    return samePassports


def suspiciouslyDealsTwo(repeatPassports): # 3 и более смены мест + промежутки между снятиями небольшие

    print(type(repeatPassports), dir(repeatPassports))
    for numberPas in repeatPassports.keys():
        if len(repeatPassports[numberPas]) > 3:
            isToOften = False
            isSameOperation = False

            startTime = repeatPassports[numberPas][0].date
            firstOpperation = repeatPassports[numberPas][0].operType
            for i in range(len(repeatPassports[numberPas])):
                object = repeatPassports[numberPas][i]
                if i != 0:
                    timeDifference = object.date - startTime
                    if timeDifference.total_seconds() < timeDelta.total_seconds(): isToOften = True
                    if firstOpperation == object.operType: isSameOperation = True
                else:
                    timeDifference = None
                # print(object.city, object.date, object.amount, object.terminal[0:3], object.operType, str(timeDifference), isSameOperation)

            if (isToOften and isSameOperation):
                print("TRUE")
                reduceRank(object,
                           penaltyForSameOftenOperationPas)  # вектор не уточнён, требуется доработка, потенциальный фрод, при уточнении, недостаточноть входных данных

