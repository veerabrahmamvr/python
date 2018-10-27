
x=3
y=3
z=3
#All three variables are pointing to same values
#We are calling that variable with different names
print (id(x),id(y),id(z))

#we are changing value for int object so it will create new address
z=4
print (id(x),id(y),id(z))



name=["veera","brahmam"]
another_name=name
print (name)
print (another_name)
print (id(name))
print (id(another_name))

#after assign changing specific element in one list will impact on another list(address will same for both list)
another_name[1]="nani"
print (name)
print (another_name)
print (id(name))
print (id(another_name))


#for assigning all elements to list will create new address for that list
another_name=["nani","test"]
print (name)
print (another_name)
print (id(name))
print (id(another_name))



#Deep copy while createing second list using 1st one
change=("veera","brahmam")
change_name=name[:]
print (change)
print (change_name)
print (id(change))
print (id(change_name))


lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[0] = 'c'
print(lst1)
print(lst2)
print (id(lst1))
print (id(lst2))
print (id(lst1[2]))
print (id(lst2[2]))



bang = ['k','l',['mn','op']]
hyd = bang.copy()
print (bang)
print (hyd)
print (id(bang))
print (id(hyd))
print (id(bang[2]))
print (id(hyd[2]))

hyd[2][1]="qr"
print (bang)
print (hyd)
print (id(bang[2]))
print (id(hyd[2]))




import copy
bang = ['k','l',['mn','op']]
hyd = copy.deepcopy(bang) 
print (bang)
print (hyd)
print (id(bang))
print (id(hyd))

hyd[2][1]="qr"
print (bang)
print (hyd)


