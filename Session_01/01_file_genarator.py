import os

for x in range(100):
	os.mkdir("Folder_"+str(x+1))
	for y in range(x):
		with open(f"Folder_{x+1}\\File_"+str(y+1)+".txt", 'w') as f:
			f.write(f"This if file {y+1} in the folder {x+1}")