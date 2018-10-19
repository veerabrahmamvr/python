#!/usr/bin/python
#This is defined list , plese change as per your need
act_list=[99999999,100,10,1000]

#This function will return the bggest number in the list
def Findmax (act_list):
    max = act_list[0]
    for i in act_list:
        if i > max:
            max=i
    return max

#This to check if the list is empty of not
if len(act_list) != 0:
    print ("Biggest Number in the given list : {}".format(Findmax (act_list)))
    print ("Index Position is : %d"%(act_list.index(Findmax(act_list))))
else:
    print ("\nList has no elements")

