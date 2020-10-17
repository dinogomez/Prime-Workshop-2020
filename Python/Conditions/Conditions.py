#booleans
#booleans = true or false // in c++ true or false also 1 or 0

#Conditional Operators if

numA = 1
numB = 2

if(numA > numB):
    print("greater")
else:
    print("lesser")

# Conditions in Python
# > - Greater than
# < - Lesser Than
# == - equals
# && - and 
# || - or

print("\nLesser than Section")
if(numA < numB):
    print("It is smaller")


#Equals Operator

print("\nEquals Section")
numA = 15
numB = 3 * 5


#It is allowed to perform Arithmetic Operations inside variable declarations
numC = 15 * 3 + 2 / 5
numD = 19 * 12 * 3 - 23

if(numC == numD):
    print("Equal")
else:
    print("Not Equal")



print("\nAND CONDITIONS")
#AND Conditions
numA = 5
#1st Condition = numA > 1 must be greater
#2nd Condition = numA < 6 must be smaller / lesser

if(numA > 1 and numA < 6):
    print("Both Conditions are met")


print("\nOR CONDITIONS")

numA = 50

if(numA > 30 or numA == 200):
    print("Conditions are met")


#To diffrentiate AND from OR : 
#AND needs All Conditions to be True
#OR needs "atleast" 1 condition

numB = 1
# true          false      false
if(numB == 1 or numB > 2 or numB> 3):
    print("Yup its still true")


