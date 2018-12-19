import json
import glob
import os
synsets = open("classes.txt").readlines()
synsets = [x.split(" ")[0].split("=")[1] for x in synsets]
files = glob.glob("*.tar.gz")
i = 0
for file in files:
	name = file.split(".")[0]
	if name not in synsets:
		os.remove(file)
	else:
		i+=1	
print(i)
