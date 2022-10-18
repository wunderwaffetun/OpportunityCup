import os
from Sheet import *
def exportToFile(transactionsList):
    
    exportData = open(f'{os.path.dirname(os.getcwd())}/py/exportData.txt', 'w+', encoding='utf-8')
    exportData.seek(0)
    SuspiciouTtransactionsNumbers = [[]]
    FraudsName = [[]]
    ErrorDataName = [[]]
    Ranks = []
    countAllElements = 0
    countNightTime = 0
    countOftenOperation = 0
    countPosTerminal = 0
    countNoValid = 0
    countClientAge = 0
    countDiffData = 0
    countSumFraud = 0
    countSumError = 0
    countChangeCity = 0 
    countAtvTerminal = 0
    clearingSheet()
    for transactionsObject in transactionsList:
        if(transactionsObject.get_rank() < fraudOperationValue):
            countAllElements += 1
            exportData.write(
                f"{transactionsObject.get_number()} {transactionsObject.get_fraud_patterns() if transactionsObject.get_fraud_patterns() != set() else 'Нет паттернов'} {transactionsObject.get_incorrect_data() if transactionsObject.get_incorrect_data() != set() else 'Нет ошибок'} {transactionsObject.get_rank()}\n")
            SuspiciouTtransactionsNumbers.append([transactionsObject.get_number()])
            Ranks.append([transactionsObject.get_rank()])
            FraudsName.append([])
            if (transactionsObject.get_fraud_patterns() != set()):
                countSumFraud+=1
            if (transactionsObject.get_incorrect_data() != set()):
                countSumError+=1

            for obj in transactionsObject.get_fraud_patterns():
                FraudsName[countAllElements].append(obj)
                
                if (obj == "NIGHT_TIME") :
                    countNightTime+=1
                if (obj == "OFTEN_SAME_OPERATIONS") :
                    countOftenOperation+=1
                if (obj == "POS_TERMINAL") :
                    countPosTerminal+=1
                if (obj == "PASSPORT_OR_ACCOUNT_NO_VALID") :
                    countNoValid+=1
                if (obj == "OFTEN_CHANGE_CITY") :
                    countChangeCity+=1
                if (obj == "CASH_OUT_ATM_TERMINAL") :
                    countAtvTerminal+=1

            ErrorDataName.append([])
            for obj in transactionsObject.get_incorrect_data():
                ErrorDataName[countAllElements].append(obj)
                
                if (obj == "INCORRECT_CLIENT_AGE") :
                    countClientAge+=1
                if (obj == "DIFFERENT_DATA") :
                    countDiffData+=1   

    exportData.write(f"{countAllElements} - всего")
    exportData.close()

    importToSheet('List2!A1:B1', [["CountAllList:", countAllElements]])
    importToSheet('List2!A2:A2', [["FraudName"]])
    importToSheet('List2!A3:B3', [["NIGHT_TIME:", countNightTime]])
    importToSheet('List2!A4:B4', [["POS_TERMINAL:", countPosTerminal]])
    importToSheet('List2!A5:B5', [["PASSPORT_OR_ACCOUNT_NO_VALID:", countNoValid]])
    importToSheet('List2!A6:B6', [["OFTEN_SAME_OPERATIONS:", countOftenOperation]])
    importToSheet('List2!A7:B7', [["OFTEN_CHANGE_CITY:", countChangeCity]])
    importToSheet('List2!A8:B8', [["CASH_OUT_ATM_TERMINAL:", countAtvTerminal]])    
    importToSheet('List2!A9:B9', [["SUMFraud:", countSumFraud]])

    importToSheet('List2!C2:D2', [["ErrorDateName"]])
    importToSheet('List2!C3:D3', [["DIFFERENT_DATA:", countDiffData]])
    importToSheet('List2!C4:D4', [["INCORRECT_CLIENT_AGE:", countClientAge]])
    importToSheet('List2!C5:D5', [["SUMError:", countSumError]])

    importToSheet('List2!11:A11', [["Percentage of fraud"]])
    importToSheet('List2!A12:B12', [["NIGHT_TIME:",countNightTime/countSumFraud]])
    importToSheet('List2!A13:B13', [["POS_TERMINAL:", countPosTerminal/countSumFraud]])
    importToSheet('List2!A14:B14', [["PASSPORT_OR_ACCOUNT_NO_VALID:", countNoValid/countSumFraud]])
    importToSheet('List2!A15:B15', [["OFTEN_SAME_OPERATIONS:", countOftenOperation/countSumFraud]])
    importToSheet('List2!A16:B16', [["OFTEN_CHANGE_CITY:", countChangeCity/countSumFraud]])
    importToSheet('List2!A17:B17', [["CASH_OUT_ATM_TERMINAL:", countAtvTerminal/countSumFraud]])    

    importToSheet('List2!C11:C11', [["Percentage of error data"]])
    importToSheet('List2!C12:D12', [["DIFFERENT_DATA:",countDiffData/countSumError]])
    importToSheet('List2!C13:D13', [["INCORRECT_CLIENT_AGE:", countClientAge/countSumError]])

    importToSheet('List2!A19:A19', [["Percentage of all list"]])
    importToSheet('List2!A20:B20', [["NIGHT_TIME:",countNightTime/countAllElements]])
    importToSheet('List2!A21:B21', [["POS_TERMINAL:", countPosTerminal/countAllElements]])
    importToSheet('List2!A22:B22', [["PASSPORT_OR_ACCOUNT_NO_VALID:", countNoValid/countAllElements]])
    importToSheet('List2!A23:B23', [["OFTEN_SAME_OPERATIONS:", countOftenOperation/countAllElements]])
    importToSheet('List2!A24:B24', [["DIFFERENT_DATA:",countDiffData/countAllElements]])
    importToSheet('List2!A25:B25', [["INCORRECT_CLIENT_AGE:", countClientAge/countAllElements]])
    importToSheet('List2!A26:B26', [["OFTEN_CHANGE_CITY:", countChangeCity/countAllElements]])
    importToSheet('List2!A27:B27', [["CASH_OUT_ATM_TERMINAL:", countAtvTerminal/countAllElements]])   

    importToSheet('List1!A1:A1', [["Number"]])
    importToSheet('List1!B1:G1', [["FraudName","FraudName","FraudName","FraudName","FraudName","FraudName"]])
    importToSheet('List1!H1:I1', [["ErrorName","ErrorName"]])
    importToSheet('List1!J1:J1', [["Rank"]])

    rangeObjects = 'List1!A1:A' + str(len(SuspiciouTtransactionsNumbers))
    importToSheet(rangeObjects, SuspiciouTtransactionsNumbers)
    rangeFraudsName = 'List1!B1:G' + str(len(SuspiciouTtransactionsNumbers))
    importToSheet(rangeFraudsName, FraudsName)
    rangeErrorDataName = 'List1!H1:I' + str(len(SuspiciouTtransactionsNumbers))
    importToSheet(rangeErrorDataName, ErrorDataName)
    rangeRank = 'List1!J2:J' + str(len(SuspiciouTtransactionsNumbers))
    importToSheet(rangeRank, Ranks)
    