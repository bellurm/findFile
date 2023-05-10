# This program will find your looking for file in the you entered path.
# This program explained in my website: 'https://blog-cyberworm.com/blog/os-py'.
import os

path = input("Where are you looking for the file? [eg: C:/, D:/, /root, /kali etc.] > ")
get_file = input("What is the file name? > ")
for dirpath, dirNames, fileNames in os.walk(path):
    for item in fileNames:
        if item == get_file:
            print(f"[FOUND] '{get_file}' is here: {dirpath}")
            exit()
            
print(f"[NOT FOUND] '{get_file}' is not found. You can look for it in another path.")
