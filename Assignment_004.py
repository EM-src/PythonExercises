import math, time

print("Q1: Write a function that computes the length of a vector. It should accept a list or a tuple as input"
      + "\n" + "    and compute the square-root of the sum of the squares of the numbers. E.g.: for a vector"
      + "\n" + "    v=[2,7,1] the length is l=math.sqrt(2*2 + 7*7 + 1*1). The function should take one argument"
      + "\n" + "    (the list  or tuple) and return one argument (the computed length)."
      + "\n")


vectorList = []
print("Define a vector. Provide x,y and z coordinates")
for i in range (0,3):
    vectorList.append(float(input()))

def vectorLength(vectorList):
    vl = math.sqrt(pow(vectorList[0],2) + pow(vectorList[1],2) + pow(vectorList[2],2))
    return(vl)

print("The vector length of vector ",vectorList, "is ",vectorLength(vectorList), "\n")


print("Q2: Write a script that prints out a sine wave with * on the screen. Each period"
      + "\n" + "    (arguments from 0 to 2*pi) should have 80 stars. Print 10 periods (10*2*pi) - so in total"
      + "\n" + "    you will ouput 80 times 10 stars. Wait 0.01 seconds between each line.)"
      + "\n")


def sineWave(n):
    for i in range(n):
        s = math.sin(2*math.pi*i/n)
        time.sleep(0.01)
        spaces = int(40*(s+1.0))
        print("-" * spaces + "*")

for k in range(10):
    sineWave(80)
