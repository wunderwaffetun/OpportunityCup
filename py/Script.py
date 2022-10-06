import os
import json
import re
from const import *
from filtersFunc import *
from readJSON import *
from dopFunction import *

if __name__ == '__main__':
    objectsList = readJsonFile([])  #получаем список json объектов
    changeObjDates(objectsList) #заменяем строковые даты на объекты дат
    globalFilters(objectsList) #основная фильтрующая функция
# objectsList = readJsonFile([])  # получаем список json объектов
# changeObjDates(objectsList)  # заменяем строковые даты на объекты дат
# globalFilters(objectsList)  # основная фильтрующая функция
#

