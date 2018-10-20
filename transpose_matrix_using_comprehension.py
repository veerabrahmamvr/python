#!/usr/bin/python

#This is list comprehension
m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print ("Original\n",m)
T = [ [row[loop] for row in m] for loop in range(len(m[0]))]
print ("Transposed matrx:\n",T)

