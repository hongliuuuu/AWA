import pandas
import numpy as np

url = '1.csv'
dataframe = pandas.read_csv(url)  # , header=None)
array = dataframe.values
X = array[:, 1:]
print(X.shape)
for i in range(5):
    url =  str(i + 2) + '.csv'
    dataframe = pandas.read_csv(url)  # , header=None)
    array = dataframe.values
    X1 = array[:, 1:]
    print(X1.shape)
    X = np.concatenate((X, X1), axis=1)
Y = pandas.read_csv('6label.csv')
Y = Y.values

Y = Y[:, 1:]
# Y = Y.transpose()
Y = np.ravel(Y)

print(X.shape, Y.shape)