
##import required directories
import os

#root directory
directory = "D:\Adani"

for foldername, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        if filename.lower().endswith(".pdf"): # check if its pdf file
            print(os.path.join(foldername, filename)) # print path and file name

    