#!/usr/bin/python
m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
T=[]
for i in range(len(m[0])):
    lst=[]
    for row in m:
        lst.append(row[i])
    T.append(lst)
print("Original Test Matrix\n",m) 
print ("\nTransposed Test Matrix\n",T)
