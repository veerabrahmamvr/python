#!/usr/bin/python
import sys
index=2
for loop in range(int(sys.argv[1]),int(sys.argv[2])):
  if loop== 2 or loop == 3 or loop==5:
    print ("Prime Number : {}".format(loop))
    continue
  for index in range(2,int(loop/2)+1):
    if loop%index != 0:
      continue
    else:
      break
  if index == int(loop/2) and loop!=4:
    print ("Prime Number : %d "%(loop))
