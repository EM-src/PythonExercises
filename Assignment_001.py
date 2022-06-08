print("Q.1: Assign some values, compare them, multiply a string with a number etc"+"\n")
x = 3
y = 5
print("x = ", x)
print("y = ", y)
print("Is x > y? ", x > y)
print("Is x < y? ", x < y)
print("Geia sou")
print("Marianna")
a = "Geia sou"
b = "Marianna"
print(a + b)
print(a + " " + b)
print(3*b)
print(3*(" " + b))
print("\n"+"Q.2: Which number is bigger 13^1321 or 17^1234?"+"\n")
x = 13 ** 1321
z = 17 ** 1234
if x > y:
    print("x is bigger than y")
else:
    print("y is bigger than x")
print("\n"+"Q.3: How many digits are in 2^1000?"+"\n")
z = 2 ** 1000
numLen = str(z)
print("The number of digits is: " + str(len(numLen)))
print("\n"+"Q.4: Multiply a string to create a nice decorative strip"+"\n")
strip = "~*"
strip_v1 = 30 * strip
print(strip_v1)
print("\n"+"Q.5: Increment a number in a variable by 1"+"\n")
t = 1
print("t = ", t)
print("Increment t value by 1")
t +=1
print("New value is ", t)
