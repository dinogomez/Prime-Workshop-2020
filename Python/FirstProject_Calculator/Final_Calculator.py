

#Calculator Python


#Basic Addition Function
#return keyword -> sends the result back to the request
def Addition(numA, numB):
    sum = numA + numB
    return sum

#Basic Subtraction Function
def Subtraction(numA, numB):
    diff = numA - numB
    return diff

#Basic Multiplication Function
def Multiplication(numA, numB):
    prod = numA * numB
    return prod

#Basic Division Function
def Division(numA, numB):
    quo = numA / numB
    return quo

print("Hello im a Calculator what are you choices?"+ "\n1. Addition" 
      + "\n2. Subtraction"  + "\n3. Multiplication" + "\n4. Division")




choice = int(input("Enter your choice(1,2,3,4): "))

#input returns a string
#We need an integer to do math
#so we convert String to integer using int() function
numA = int(input("What is your first number: "))
numB = int(input("What is your second number: "))



#Once we have our choice dito na papasok si Conditional
#its okay to not use () if ever one operator only


# if you're gonna use if after and else always use "elif"
answer = 0
operator = ""
# 1+1 2+2   2+3 and 4+4 -> thats two operators so need ng ()
if choice == 1:
    answer = Addition(numA, numB)
    #I will this later when I will print the arithmetic equation
    operator = "+"
elif choice == 2:
    answer = Subtraction(numA,numB)
    operator = "-"
elif choice == 3:
    answer = Multiplication(numA, numB)
    operator = "*"
elif choice == 4:
    answer = Division(numA, numB)
    operator = "/"
else:
    print("Your choice is not valid")


print("\nThe answer between " + str(numA) + operator + str(numB) 
      + " = " + str(answer))







#We expect that Addition Function will return a answer
#The answer will now be stored on the variable called "Result"
#result = Addition(3,5)

#EOF ERROR = variable having () double parenthesis which are for
#functions only
#print("Result now holds the value of " + str(result))

