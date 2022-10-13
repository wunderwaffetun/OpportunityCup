
from config import *
from generalFunctions import *
from readJSON import *
from additionalFunctions import *
from main import *

def repeatPassport(objectsList):
    samePassports = dict()
    for object in objectsList:
        if object.passport not in samePassports:
            samePassports.update({object.passport: [object]})
        else:
            samePassports[object.passport].append(object)
    return samePassports

def reduceForManyPassportsOperations(objectsList, listOfPassoprtWhereTooManyOperations):
    for object in objectsList:
        if object.passport in listOfPassoprtWhereTooManyOperations:
            reduceRank(object, penaltyForSameOftenOperationPas)


def manyOperationsByOnePass(repeatPassports): # 3 и более смены мест + промежутки между снятиями небольшие
    listOfPassoprtWhereTooManyOperations = []
    for key in repeatPassports.keys():
        if len(repeatPassports[key]) > limitOperationsByPass:
            listOfPassoprtWhereTooManyOperations.append(key)
    return listOfPassoprtWhereTooManyOperations

