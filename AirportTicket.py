import pandas as pd
from sklearn.externals import joblib

filename = 'finalized_model.sav'
XGBRegressor = joblib.load(filename)

filename = 'Preprocessing_model.sav'
sc = joblib.load(filename)

print("Введите несколько параметров для определения цены")
parameter1 = int(input("Количество купонов на рынке на этот рейс: "))
parameter2 = int(input("Прелёт внутри региона/штата (да - 1 , нет - 0): "))
parameter3 = int(input("Кватал/сезон вылета: "))
parameter4 = int(input("Код места вилета: "))
parameter5 = int(input("Код места посадки: "))
parameter6 = float(input("Мили: "))
parameter7 = int(input("(2) означает, что полет находится в смежных (48) штатах США, и (1) означает, что это не так: "))
parameter8 = int(input("Количество билетов который вы хотите преобрести: "))
parameter9 = int(input("Код авиакомпании: "))

data = {'parameter1':[parameter1],'parameter3':[parameter3],'parameter4':[parameter4],'parameter5':[parameter5],'parameter6':[parameter6],'parameter7':[parameter7],'parameter8':[parameter8],'parameter9':[parameter9],'parameter2':[parameter2]}

df = pd.DataFrame(data)

ParameterList = sc.transform(df)

print("Цена на билет: ", XGBRegressor.predict(ParameterList))