#This scipt can be used when we have a large number of files in a folder which we want to name in an order
import os

#get the path of the file and the file names
path = os.getcwd()
files = os.listdir(path)

#print the file names before iteration
print(f"Before Renaming: {files}") 

#rename the files
for i in range(len(files)):
	if files[i].find(".py") != -1 :
		continue
	os.rename(files[i],f"parentfilename{i+1}.extension")
	
#print the final file names
print(f"After Renaming: {os.listdir(path)}")
