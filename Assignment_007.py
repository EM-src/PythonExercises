import os #import os to use environmental variables
import sys

print("Q1: Write a Python script that lists all the directories in the PATH environment variable. One path per line."
      + "\n")

print("Q2: Once this works: extend your script to process one command-line argument and search all directories in the path to find the first directory"
      + "\n" + "    where the file with the name given in the argument is found. e.g.: when you run ./assignment009.py fileName it would print out: /usr/bin/fileName"
      + "\n" + "    If no command-line argument is given then just print out the PATH directories."
      + "\n")

#iterate through the PATH chars, if a char is "/" then slice the environment variable PATH up to 
#that point and put it in a list
counter = 0
paths = []
for char in os.environ['PATH']:
      counter +=1
      if char == "/":
            paths.append(os.environ['PATH'][:counter])

#if sys.argv list has more than one elements then check if any of the elements when appended to a path
#from the paths list exists. If yes then print the file path and break. If a break is not detected the else
#of the for loop is executed and the message No file found is printed. In all other cases the list of paths
#are printed
if len(sys.argv) > 1:
      for arg in sys.argv:
            for path in paths:
                  if os.path.exists(path + arg):
                        print("The file path is: ", os.environ['PATH'][:counter] + arg, "\n")
                        break
      else:
            print("No file found.")
else:
      print("Paths:")
      print("\n".join(paths), "\n")