import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n")

print("1. Print tabular data\n")
df = pd.DataFrame({
    "Candidate": ["Alex", "Amy", "Boland", "Kamelia", "Lee", "Maryam", "Qasem"],
    "University": ["Northumbria", "Newcastle", "Manchester", "Liverpool", "Edinburgh", "Belfast", "Birmingham"],
    "Age": [23,24,31,29,34,41,35],
    "Exam": [73.0,78.0,80.0,84.0,72.0,81.0,80.0]
})
print(df, "\n")

print("2. Print the first 5 rows:")
print(df[0:5], "\n")

print("3. Print the last 5 rows:")
print(df[-5:], "\n")

print("4. Print all entries in University column:")
print(df.loc[:, ["University"]], "\n")

print("5. Print all entries in first row:")
print(df.loc[:0], "\n")

print("6. Print all entries in first row:")
print(df.loc[:2], "\n")

print("7. Print which university is Alex:")
print(df.loc[df["Candidate"] == "Alex", ["University"]], "\n")

print("8. Print all information about Amy:")
print(df.loc[df["Candidate"] == "Amy"], "\n")

print("9. Print the descriptive statistics of the Age column:")
print(df["Age"].describe(), "\n")

print("10. Print the descriptive statistics of both Age and Exam columns:")
print(df.describe(), "\n")

print("11. Remove or drop column University:")
dfDropCol = df.copy()
dfDropCol.drop("University", inplace=True, axis=1)
print(dfDropCol, "\n")

print("12. Remove or drop the first 3 rows:")
dfDropRow = df.copy()
dfDropRow.drop(labels=range(0,3), inplace=True, axis=0)
print(dfDropRow, "\n")

print("13. Plot a bar chart for exam vs. candidate.")
plt.bar(df["Exam"], df["Candidate"])
plt.title("Q.13: Exam vs Candidate")
plt.show()
