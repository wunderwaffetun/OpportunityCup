import datetime

penaltyForNightTime = 3
penaltyForRejectionAndFrod = 3
penaltyForSameOftenOperationPas = 30 #Новый паттерн 
penaltyForSameOftenOperationCart = 7
penaltyForWithdrawalATM = 9
penaltyForRefillPOS = 11
penaltyForVisetedCities = 11
penaltyForValidTo = 17
penaltyForPasError = 31


firstStartFunctionDeals = True #Чтобы не накладывался штраф за города и за одинаковые карты и за паспорта несколько раз
quantityOperationsByOneCardOrPass = 1 # константа, которая определят от скольки операций мы опрделяем "Слишком часто"
deltaSiriesInYearIssuance = 3
limitMinAgeForPas = 14
limitWithdrawalATM = 20000
limitCountVisitedCities = 1
limitMinYearPas = 1996 #c 97 выдача паспорта РФ
limitMaxYearPas = 2023 #год из серии не превышает нынешний
limitMaxAge = 100
# limitOperationsByPass = 10
NextYear = 23
rank = 100
includeSameOperations = False #учитываем что операции одинаковые (для фрода)
fraudOperationValue = 78 #с какого ранга мы считаем людей мошенниками 
timeDelta = datetime.timedelta(hours=24) # минимальный промежуток для сниятия

link = ['https://www.googleapis.com/auth/spreadsheets']#права  на работу с таблицей
idLink = '1kRN1VcA99_12FRJSDLhqwpqzPPY3WXzp_BPTFqF_OG4'#id таблицы (/d/*оно_самое*/edit)
data = 'TestList!A2:G7'#с какими данными работаем (книга и ячейки)
