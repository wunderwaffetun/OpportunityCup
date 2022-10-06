import datetime
penaltyForNightTime = 1
penaltyForVisetedCities = 9
penaltyForSameOftenOperation =9
penaltyForWithdrawalATM = 7
penaltyForValidTo = 10
penaltyForPasError = 5
penaltyForRefillPOS = 2
penaltyForRejectionAndFrod = 1
deltaSiriesInYearIssuance = 3
limitMinAgeForPas = 14
limitWithdrawalATM = 20000
limitCountVisitedCities = 3
limitMinYearPas = 1996 #c 97 выдача паспорта РФ
limitMaxYearPas = 2023 #год из серии не превышает нынешний
limitMaxAge = 100
nowYear = 23
rank =50
timeDelta = datetime.timedelta(hours=3) # минимальный промежуток для сниятия