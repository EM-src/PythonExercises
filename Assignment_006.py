
print("Q1: Write a python script that reads a file named \"accounting.csv\" and prints it nicely formated as table."
      + "\n" + "    The structure is 3 fileds separated with TAB characters where the 1st is cost center, the 2nd "
      + "\n" + "    is product and the 3rd is amount. Sum up the \"amount\" number for all the products. Keep your sums in a dictionary."
      + "\n")

file = open("/Users/manosmarketos/Desktop/PythonExercises/accounting.csv", "rt")

prodSum = {}
#count = 0
print("*--------------------------------*")
print("| Cost_Center | Product | Amount |")
print("|--------------------------------|")
for line in file:
    l  = line.rstrip().split("\t") #Creating a list from each .csv row
    cc = l[0].strip()              #getting each list element from the list stripped from spaces
    prod = l[1].strip()
    amount = float(l[2].strip())   #casting the last elemnt which is of type string to float
    print(f"| {cc:11s} | {prod:7s} | {amount:6.2f} |") #Formatting so we can print the output in a table visual style
    prodSum[prod] = prodSum.get(prod,0.0) + amount

print("*--------------------------------*" + "\n\n")
#print(prodSum)
print("*------------------*")
print("| Product | Amount |")
print("|------------------|")
for product, amount in prodSum.items():
    print(f"| {product:7s} | {amount:6.2f} |")
print("*------------------*" + "\n\n")
file.close()
