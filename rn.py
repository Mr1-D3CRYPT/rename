import os

path = os.getcwd()

print(path)
files = os.listdir(path)

print(f"Before Renaming: {files}")
for i in range(len(files)):
	if files[i].find(".py") != -1 :
		continue
	os.rename(files[i],f"night{i+1}.jpg")
print(f"After Renaming: {os.listdir(path)}")
