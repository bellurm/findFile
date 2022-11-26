# For the Windows users.
# This program will find your looking for file in the you entered path.
# This program explained in my website: 'https://blog-cyberworm.com/blog/os-py'.
import os

for dirpath, dirNames, fileNames in os.walk("C:/"): #You can change the target path like 'D:/'.
    for item in fileNames:
        if item == "CHANGE ME - File Name":
            print(dirpath)
            exit()
