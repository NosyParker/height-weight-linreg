# -*- coding: utf8 -*- 
import pandas
import matplotlib.pyplot as plt

data_for_computing = pandas.read_csv("data.csv", sep=",", index_col="Index")

#print (data_for_computing["Weight"].tolist())
plt.plot(data_for_computing["Height"].values, data_for_computing["Weight"].values,'go')
plt.xlabel('Рост (дюймы)') #Метка по оси x в формате TeX
plt.ylabel('Вес (футы)') #Метка по оси y в формате TeX
plt.title('Зависимость веса от роста') #Заголовок в формате TeX
plt.grid(True) #Сетка
plt.show()
#print (data_for_computing)
