import pandas


data_for_computing = pandas.read_csv("data.csv", sep=",", index_col="Index")

print (data_for_computing)
