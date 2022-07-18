
print("Q1: Create a python script that reads all lines of a file and prints them with line numbers. Then use either"
      + "\n" + "    % formatting or f-string interpollation so that the line numbers always take up to 6 digits.Find"
      + "\n" + "    out what happens when you do not open your file with 'rt' (read text) but with 'rb' (read binary)."
      + "\n")

line_nr = 0

f = open("/Users/manosmarketos/Desktop/PythonExercises/Read_From_file_test.txt", "rt")
for line in f:
    print("line:", f"{line_nr:3d}",":", line.rstrip())
    line_nr += 1

f.close()
