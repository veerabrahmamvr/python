#!/usr/bin/python

#This is to enerate Random numers
import numpy

#This packgae is for progress bar testing 
import tqdm

#Sleep few sel in loop
import time

#Just Generating random numbers & looping over it using tqdm
for random_num in tqdm.tqdm(numpy.random.random_integers(low=1,high=1000,size=50)):
    time.sleep(1)
    final_num = random_num * 100
   
    
