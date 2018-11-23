#! /usr/bin/python
import os

dirName = raw_input("Enter the path were you want to create a new dirtectory:  ")
os.mkdir('dirName')

#xcept FileExistsError:
#   print("Directory " , dirName ,  " already exists")
if not os.path.exists(dirName):
   os.mkdir(dirName)
   print("Directory " , dirName ,  " Created ")
else:
   print("Directory " , dirName ,  " already exists")