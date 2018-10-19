#!/usr/bin/python
"""If u increase the I/P value to any extent time will take almost neglegible"""
import time
ini_time=time.time()
def SumOfN(n):
  return n*(n+1)/2
fin_time=time.time()
print ("Time Take %f"%(fin_time-ini_time))
print (SumOfN(900000))
