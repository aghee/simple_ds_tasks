"""
#fewer values in dictionary
counts=dict()
names=['a','b','a','d','l','m','a','l','n ','n ','n ','d','d','a','z','a','d','m','b','a','a','a']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)
#import matplotlib to view histogram, or use jupyterlab for histogram
import matplotlib.pyplot as plt
keys=list(counts.keys())
values=list(counts.values())
plt.bar(range(len(counts)),values,tick_label=keys)
plt.show()
"""
#more values in dictionary
fname=input('enter file name:')
fhand=open(fname)
#print(fhand.read())

for name in fhand:
    var1=name.split()
    #print(var1)
dictone={}
for name in var1:
    dictone[name]=dictone.get(name,0)+1
print(dictone)
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
keys=list(dictone.keys())
values=list(dictone.values())
#vals=[2,5,8,7,9,8,7,2,5,4]
#bar graph
plt.bar(range(len(dictone)),values,tick_label=keys)
#scatter plots
#plt.scatter(keys,values)
#pie charts
#fig = plt.figure(figsize =(10, 7))
#plt.pie(vals, labels = var1)
plt.show()