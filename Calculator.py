 
print("Welcome to Aarya's Calculator")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
Operations = ("""To perform specific operation press "1" for addition""",
              """"2" for subtraction""", """"3" for multiplication""",
              """"4" for division""")
for Operation in Operations:
  print(Operation)
Perform = input("Enter the operation you want to perform: ")
if (Perform == "1"):
  print("The value of", a, "+", b, "is:", a + b)
elif (Perform == "2"):
  print("the value of", a, "-", b, "is:", a - b)
elif (Perform == "3"):
  print("the value of", a, "*", b, "is:", a * b)
elif (Perform == "4"):
  print("The value of", a, "/", b, "is:", a / b)
else:
  print("Invalid Input")