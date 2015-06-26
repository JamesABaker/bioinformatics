#Converts X.txt and Y.txt to Wilcoxon rank-sum values.

'''
A sample file contains:

1.8
1.5
1.3
'''

#Numpy is also needed for scipy to work properly I think...
import scipy
from scipy import stats

#These lists hold the two datasets
x=[]
y=[]

#This opens the x and y files line by line and imports each value as a new value in the lists.
with open ("x.txt", "r") as xfile:
    for a in xfile.read().split():
        x.append(a)

with open ("y.txt", "r") as yfile:
    for b in yfile.read().split():
        y.append(b)

#Now the datasets have the values in, we can use the scipy ranksum module.
print "test: (z-statistic, p-value)"
print "The Wilcoxon rank-sum test:", scipy.stats.ranksums(x, y)
if len(y)==len(x):
    print "Wilcoxon signed-rank test:", scipy.stats.wilcoxon(x, y)
else:
    print "Unequal N in x.txt and y.txt so a Wilcoxon signed-rank test cannot be applied."
