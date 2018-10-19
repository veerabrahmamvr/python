#!/usr/bin/python 
"""If u increase the I/P value to any extent time  take Increase\
test
"""
import time
def SumOfN(n):
  ini_time=time.time()
  sum=0
  for i in range(n+1):
    sum=sum+i
  fin_time=time.time()
  return sum,fin_time-ini_time
    
print (SumOfN(900000))
