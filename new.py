# -*- coding: utf8 -*-

import pandas
import matplotlib.pyplot as plt
from scipy import stats
import math
data_for_computing = pandas.read_csv("data.csv", sep=",", index_col="Index")

x = data_for_computing["Height"].values
y = data_for_computing["Weight"].values

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

print ('Коэффициент K:', slope)
print  ('Коэффициент b:', intercept)
print ('Стандартное отклонение:', std_err)
print ('Коэффициент корреляции:', r_value)

line = slope*x+intercept

err_rmse =math.sqrt(sum((line-y)**2)/len(y))

real_wf = slope*70.08 + intercept
real_wkg = real_wf*0.454
print ("Корень среднеквадратичной ошибки (RMSE):", err_rmse )

print ("Вес в фунтах: {0}, а в кг: {1}".format(real_wf, real_wkg))
plt.plot(x, y,'go')
plt.plot(x, line, color='red')
plt.xlabel('Рост (дюймы)')
plt.ylabel('Вес (футы)')
plt.title('Зависимость веса от роста')

plt.grid(True)
plt.show()