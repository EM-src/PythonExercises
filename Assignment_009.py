import os
import sys
import time
import mytime_009

# Main program using the custom module mytime_009. Gets the files to be checked as input from
# terminal and puts them in a list.

def listfiles(filenames):
    currTime = time.time()
    for file in filenames:
        modt = mytime_009.mtime(file)
        if modt == None:
            print("file {} does not exist.".format(file))
        else:
            print("file {} is {:0.3f} seconds old.".format(file, currTime-modt))

print("my context: ",__name__)
if __name__ =="__main__":
    print(sys.argv[1:])
    listfiles(sys.argv[1:])
