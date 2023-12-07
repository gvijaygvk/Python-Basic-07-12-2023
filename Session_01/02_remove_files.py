import os
for x in range(100):
	for y in range(x):
		if os.path.exists(f"Folder_{x+1}\\File_"+str(y+1)+".txt"):
			os.remove(f"Folder_{x+1}\\File_"+str(y+1)+".txt")
	if os.path.exists(f"Folder_{x + 1}"):
		os.rmdir("Folder_" + str(x + 1))