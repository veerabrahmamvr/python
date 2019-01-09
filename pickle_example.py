#pickling in python implements binary protocol for serializing and deserializing python objects.
import pickle
import numpy

#creating dictionary with random variables
data = {"veera":numpy.random.random(10),"brahmam":numpy.random.random(10)}

#opening the pkl file to load the data in to pickle file (so write binary format)
with open ("test_data.pkl",'wb') as fd_write:
    pickle.dump(data,fd_write)  # this will dump entire serialized data in to file


print (data) # this will print object data
del data #deleted object , so we can't access ny more 

try:
    print (data) # try to access deleted object, it throws error
except:
    print ("data object is not found")#exception is expected , so handling

#Now LOAD and read data from pickling file for deleted object
with open ("test_data.pkl","rb") as fd_read:
    load_object = pickle.load (fd_read)
    
print (load_object)
print ("Testinggggg",load_object["veera"][0])
