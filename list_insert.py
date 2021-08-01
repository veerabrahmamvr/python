list1=["arm","x86","powerpc","Micro Controler"]
list2=["windows","linux","unix"]


"""
this prgram to insert second list elements in to specific inex
"""
j=0
for i in list2:
   list1.insert(2+j,i)
   j+=1

print (list1)

test_list=["veera","brahmam","vannem", "reddi"]
test_names=["baby sarojini","bhaskara rao"]
test_append=["baby"]

"Extend will add second list elements one by one in to first list"
test_list.extend(test_names)


"""
append add complete second as a single element for 1st list
"""
print (test_list)
test_list.append(test_append)
print (test_list)


list3=[9,4,1,0,3,2]
list3.sort(reverse=True)
print (list3)


tuple01=(99,54,22,76)
print (tuple01)
