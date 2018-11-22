#/usr/bin/python
"""zip wraps two or more iterators with a lazy generator. The zip generator yields
tuples containing the next value from each iterator."""

#iterate  both lists in parallel

list_test = ["veera","brahmam","vannem","reddi"]
list_test_lengths = [ len(i) for i in list_test] 
for  name,lens in  zip( list_test , list_test_lengths):
  print (" Name : %s  length is %d"%(name,lens))

count=0
longest_name=""
for  name,lens in  zip( list_test , list_test_lengths):
  if lens > count:
    count = lens
    longest_name = name
print (longest_name)
    
