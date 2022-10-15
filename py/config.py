import datetime

penaltyForNightTime = 3
penaltyForRejectionAndFrod = 3
penaltyForSameOftenOperationPas = 5
penaltyForSameOftenOperationCart = 7
penaltyForWithdrawalATM = 9
penaltyForRefillPOS = 11
penaltyForVisetedCities = 13
penaltyForValidTo = 17
penaltyForPasError = 50

quantityOperationsByOneCardOrPass = 1 # константа, которая определят от скольки операций мы опрделяем "Слишком часто"
deltaSiriesInYearIssuance = 3
limitMinAgeForPas = 14
limitWithdrawalATM = 20000
limitCountVisitedCities = 3
limitMinYearPas = 1996 #c 97 выдача паспорта РФ
limitMaxYearPas = 2023 #год из серии не превышает нынешний
limitMaxAge = 120
limitOperationsByPass = 10
NextYear = 23
rank = 100
includeSameOperations = False #учитываем что операции одинаковые (для фрода)
fraudOperationValue = 90 #с какого ранга мы считаем людей мошенниками 
timeDelta = datetime.timedelta(hours=24) # минимальный промежуток для сниятия