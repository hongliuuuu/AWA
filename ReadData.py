from os import walk
import pandas
import numpy as np
import random
f = []
mypath = "data"
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(dirnames)
    break

newpath = []

for i in range(len(f)):
    p = mypath+"/"+f[i]
    newpath.append(p)
print(newpath)

dp = "data/surf-hist"
cl = []
for (dirpath, dirnames, filenames) in walk(dp):
    cl.extend(dirnames)
    break
print(len(cl))



X = []
Y = []
for j in range(len(cl)):
    newdp = dp+"/"+cl[j]


    ob = []
    for (dirpath, dirnames, filenames) in walk(newdp):
        ob.extend(filenames)
        break
    ob = random.Random(1000+j).sample(ob,k=80)
    for i in range(len(ob)):
        p = newdp + "/"+ob[i]
        dataframe = pandas.read_csv(p, header=None, delim_whitespace=True)
        array = dataframe.values
        X.append(array[0])
        Y.append(j)



Y = np.array(Y)
#X = np.array(X)
#print(X.shape)
print(Y.shape)

prediction = pandas.DataFrame(X).to_csv('6.csv')
prediction = pandas.DataFrame(Y).to_csv('6label.csv')