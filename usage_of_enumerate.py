#/usr/bin/python3 

flavours_icecream = ["vanilla", "chocolate", "pecan", "strawberry"]

for flavour in flavours_icecream:
  print (flavour)

# If we want Ranking of the ICE cream flavours
for i in range(len(flavours_icecream)):
  print ("%d : %s"%(i+i, flavours_icecream[i]))


"""Generally Above solutoion is Visually Noiseeee & there is   RANK 0  for Vanilla\
which looks dirrent"""

# USe Enumerator 

for i,flvr in enumerate(flavours_icecream,10):
  print ("Rank : %d , %s Ice Cream"%(i,flvr))
