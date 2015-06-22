#Converts X.txt and Y.txt to Wilcoxon rank-sum values.

'''
A sample file contains:

1.819047619
1.561904762
1.476190476
1.471428571
1.316666667
1.300334448
1.3
1.252380952
1.242857143
1.223809524
1.2
1.123809524
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
print "(z-statistic, p-value)"
print scipy.stats.ranksums(x, y)
