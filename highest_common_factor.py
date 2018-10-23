#!/usr/bin/python
import sys
def hcf (i,j):
    hcf_value = min(i,j)
    if i==j or i%j==0 or j%i==0:
        return hcf_value
    for k in range (1,hcf_value//2):
        if i%k==0 and j%k==0:
            hcf_value=k
    return hcf_value

    
print ("{0},{1} highe common factore is {2}".format(sys.argv[1],sys.argv[2],hcf(int(sys.argv[1]),int(sys.argv[2]))))
