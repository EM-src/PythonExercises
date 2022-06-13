import math
print("Q1: Use a loop to sum the first 100 numbers starting from 1 and" +
      "\n" + "    then compute the product of those numbers. How many digits does" +
      "\n" + "    the product have? (the computation will take a few seconds)" +
      "\n")

sumOfNumbers = 0
for a in range(1, 101):
    sumOfNumbers = sumOfNumbers + a

print("Sum from 1 to 100 is: ", sumOfNumbers, "\n")

productOfNumbers = 1
for a in range(1, 101):
    productOfNumbers = productOfNumbers * a

numOfDigits = len(list(str(productOfNumbers)))

print("The product of 1 to 100 is:" + "\n", productOfNumbers, "\n" + "and it has", numOfDigits,
      "digits" + "\n")

print("Q2: Use a loop to create a list of the first 100 square numbers (starting" +
      "\n" + "    with 1)" + "\n")

sqrNums = list()
for a in range(1,101):
    if str(math.sqrt(a)).endswith('.0'):
        sqrNums.append(a)
print(sqrNums, "\n")

print("Q3: Write a loop that picks the first and then every second element from" +
      "\n" + "    a list and creates a new list with that eg: from [1,2,3,4,5,6]" +
      "\n" + "    it would pick [1,3,5]. Check if it works for lists with even" +
      "\n" + "    odd numbers." + "\n")

evenList = list()
for i in range(1,21):
    evenList.append(i)

oddList = list()
for i in range(1,22):
    oddList.append(i)

print("Even list defined as:" + "\n", evenList)
print("Odd list defined as:" + "\n", oddList, "\n")

newList = list()
for i in range(1, len(evenList)+1, 2):
    newList.append(evenList[i-1])

print("New list from even list with every second element:" + "\n", newList)

newList = list()
for i in range(1, len(oddList)+1, 2):
    newList.append(oddList[i-1])
    
print("New list from odd list with every second element:" + "\n", newList, "\n")

print("Q4: Compute the first 100 Fibonacci numbers." +
      "\n" + "    F0 = 0, F1 = 1, ..., Fn = Fn-1 + Fn-2. Which means the first" +
      "\n" + "    number is 0 the next is 1 and each of the following is the sum of" +
      "\n" + "    the two previous ones. Print your output and also store it in a" +
      "\n" + "    list. So the Fiboinacci numbers are: 0,1,1,2,3,5,8,13,21..." + "\n")

Fib = [0,1]
for i in range(98):
    Fib.append(Fib[-1] + Fib[-2])

print("Fibonacci series from 0 to 100 is" + "\n", Fib)
