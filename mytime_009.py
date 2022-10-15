import os
import sys
import time

# Function to have as an input a file name and calculating when it was lastly modified
# it returns the modtime in seconds if the file was found and None if it is not found
def mtime(filename):
    modtime = None
    if os.path.exists(filename):
       modtime = os.stat(filename).st_mtime
       #mod time is in seconds
       days = (time.time()-modtime)/(60*60*24)
       #print(modtime,"seconds till last modification", "\n", days, " days since last modification")
    else:
        print("File not found")
    return modtime

#print("my context: ",__name__)
#if __name__ == "__main__":
#    mtime("Assignment_00.py")

