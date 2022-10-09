print("Q1: Write a Python script that lists all the directories in the PATH environment variable. One path per line."
      + "\n")

print("Q2: Change your script so that each line is terminated with a / (on unix). If you want to be platform independent you can use os.path.sep."
      + "\n")

print("Q2: Once this works: extend your script to process one command-line argument and search all directories in the path to find the first directory"
      + "\n" + "    where the file with the name given in the argument is found. e.g.: when you run ./assignment009.py ping it would print out: /usr/bin/ping"
      + "\n" + "    (or /bin/ping depending on where it is found first). If no command-line argument is given then just print out the PATH directories (like in point 2)."
      + "\n" + "    To make things simple: We do not check if the file is executable or not. Just check if it exists. os.path.exists(\"/some/file/name\")"
      + "\n" + "    will tell you if the file exists.So your program  will do the same thing as the unix program named \"which\", which also looks"
      + "\n" + "    up the path and prints out the name of the file that is executed."
      + "\n")