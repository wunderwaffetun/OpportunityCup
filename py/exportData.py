import os
from config import *
from generalFunctions import *
from readJSON import *
from additionalFunctions import *
from exportData import *
from Sheet import *


def exportToFile(objectsList):
    count = 0
    exportData = open(f'{os.path.dirname(os.getcwd())}/py/exportData.txt', 'w+', encoding='utf-8')
    exportData.seek(0)
    Objects=[[]]
    FraudsName=[[]]
    ErrorDataName=[[]]
    PatternList = []
    ErrorList = []
    Ranks = []
    countNightTime=0
    countOftenOperation=0
    countPosTerminal=0
    countNoValid=0
    countClientAge=0
    countDiffData=0
    countSumFraud=0
    countSumError=0
    for object in objectsList:
        if(object.get_rank() < fraudOperationValue):
            count += 1
            exportData.write(f"{object.get_number()} {object.get_fraud_patterns() if object.get_fraud_patterns() != set() else 'Нет паттернов'} {object.get_incorrect_data() if object.get_incorrect_data() != set() else 'Нет ошибок'} {object.get_rank()}\n")
            Objects.append([object.get_number()])
            Ranks.append([object.get_rank()])
            FraudsName.append([])
            if (object.get_fraud_patterns() != set()):
                countSumFraud+=1
            if (object.get_incorrect_data() != set()):
                countSumError+=1
            for obj in object.get_fraud_patterns():
                FraudsName[count].append(obj)
                PatternList.append(obj)
                
                if (obj == "NIGHT_TIME") :
                    countNightTime+=1
                if (obj == "OFTEN_SAME_OPERATIONS") :
                    countOftenOperation+=1
                if (obj == "POS_TERMINAL") :
                    countPosTerminal+=1
                if (obj == "PASSPORT_OR_ACCOUNT_NO_VALID") :
                    countNoValid+=1
            ErrorDataName.append([])
            for obj in object.get_incorrect_data():
                ErrorDataName[count].append(obj)
                ErrorList.append(obj) 
                
                if (obj == "INCORRECT_CLIENT_AGE") :
                    countClientAge+=1
                if (obj == "DIFFERENT_DATA") :
                    countDiffData+=1         
            # # exportData.write(f"{object.fraudPatterns}")
            # rangeObj = 'TestList!A' + str(count + 1) + ':A' + str(count + 1)
            # valuesObj = [[object.get_number()]]
            # importToSheet(rangeObj, valuesObj)
    exportData.write(f"{count} - всего")
    exportData.close()
    PatternList = set(PatternList) 
    ErrorList = set(ErrorList) 
    #print(ErrorList)
    #print(PatternList)

    importToSheet('List2!A1:B1', [["CountAllList:", count]])
    importToSheet('List2!A2:A2', [["FraudName"]])
    importToSheet('List2!A3:B3', [["NIGHT_TIME:", countNightTime]])
    importToSheet('List2!A4:B4', [["POS_TERMINAL:", countPosTerminal]])
    importToSheet('List2!A5:B5', [["PASSPORT_OR_ACCOUNT_NO_VALID:", countNoValid]])
    importToSheet('List2!A6:B6', [["OFTEN_SAME_OPERATIONS:", countOftenOperation]])
    importToSheet('List2!C2:D2', [["ErrorDateName"]])
    importToSheet('List2!C3:D3', [["DIFFERENT_DATA:", countDiffData]])
    importToSheet('List2!C4:D4', [["INCORRECT_CLIENT_AGE:", countClientAge]])
    importToSheet('List2!A7:B7', [["SUMFraud:", countSumFraud]])
    importToSheet('List2!C5:D5', [["SUMError:", countSumError]])

    importToSheet('List2!A9:A9', [["Percentage of fraud"]])
    importToSheet('List2!A10:B10', [["NIGHT_TIME:",countNightTime/countSumFraud]])
    importToSheet('List2!A11:B11', [["POS_TERMINAL:", countPosTerminal/countSumFraud]])
    importToSheet('List2!A12:B12', [["PASSPORT_OR_ACCOUNT_NO_VALID:", countNoValid/countSumFraud]])
    importToSheet('List2!A13:B13', [["OFTEN_SAME_OPERATIONS:", countOftenOperation/countSumFraud]])

    importToSheet('List2!C9:C9', [["Percentage of error data"]])
    importToSheet('List2!C10:D10', [["DIFFERENT_DATA:",countDiffData/countSumError]])
    importToSheet('List2!C11:D11', [["INCORRECT_CLIENT_AGE:", countClientAge/countSumError]])

    importToSheet('List2!A15:A15', [["Percentage of all list"]])
    importToSheet('List2!A16:B16', [["NIGHT_TIME:",countNightTime/count]])
    importToSheet('List2!A17:B17', [["POS_TERMINAL:", countPosTerminal/count]])
    importToSheet('List2!A18:B18', [["PASSPORT_OR_ACCOUNT_NO_VALID:", countNoValid/count]])
    importToSheet('List2!A19:B19', [["OFTEN_SAME_OPERATIONS:", countOftenOperation/count]])
    importToSheet('List2!A20:B20', [["DIFFERENT_DATA:",countDiffData/count]])
    importToSheet('List2!A21:B21', [["INCORRECT_CLIENT_AGE:", countClientAge/count]])

    importToSheet('List1!A1:A1', [["Number"]])
    importToSheet('List1!B1:E1', [["FraudName","FraudName","FraudName","FraudName"]])
    importToSheet('List1!F1:G1', [["ErrorName","ErrorName"]])
    importToSheet('List1!H1:H1', [["Rank"]])
    rangeObjects = 'List1!A1:A' + str(len(Objects))
    importToSheet(rangeObjects, Objects)
    rangeFraudsName = 'List1!B1:E' + str(len(Objects))
    importToSheet(rangeFraudsName, FraudsName)
    rangeErrorDataName = 'List1!F1:G' + str(len(Objects))
    importToSheet(rangeErrorDataName, ErrorDataName)
    rangeRank = 'List1!H2:H' + str(len(Objects))
    importToSheet(rangeRank, Ranks)