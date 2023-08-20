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
import matplotlib.pyplot as plt
keys=list(dictone.keys())
values=list(dictone.values())
plt.bar(range(len(dictone)),values,tick_label=keys)
plt.show()