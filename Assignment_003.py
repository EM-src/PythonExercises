import math

print("Q1: The sum of all 1 +1/2 + 1/3 + 1/4 + 1/5 + ... +1/n (also known as the harmonic series)"
      + "\n" + "    grows to infinity as the number of terms (n) grows, but only very very slowly."
      + "\n" + "    How many terms do we have to sum (that is how big must n be) in order to get"
      + "\n" + "    a sum that is even larger than 15?"
      + "\n")

a = 0
n = 1
while a < 15:
    a = a + 1/n
    n += 1
print("The number of terms is",n, "for a sum of",a, "\n")

print("Q2: Bisection: We want to find a solution for the equation y=x^x where y=3. One way to"
      + "\n" + "    find this is by bisection: We know that the x we are searching for is somewhere"
      + "\n" + "    between 1 (where y=1) and 2 (since 2^2 is already 4). Now we try out the value"
      + "\n" + "    in the middle 1.5 and see if it gives a result higher or lower than 3. In the"
      + "\n" + "    first case we know that our solution is somewhere in the interval between"
      + "\n" + "    1 and 1.5, in the other case we know to search in between 1.5 and 2. If we"
      + "\n" + "    continue to divide our interval in half we find closer and closer intervals"
      + "\n" + "    where our solution is in. Find x so that the interval is below 1e-15."
      + "\n")

a = 1  #lower bound
b = 2  #upper bound
while (b-a) > pow(0.1,15):
    x = (a+b)/2
    if x**x > 3:
        b=x
    elif x**x < 3:
        a=x
print("x: ", x, " x**x:", x**x, " x is within [",a,",",b,"]")
