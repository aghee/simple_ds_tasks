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
