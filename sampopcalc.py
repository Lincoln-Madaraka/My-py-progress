#simple calc clone
#sample operation flow
num1 , operation, num2 = input("ENTER CALCULATION : ").split()
#converting strings to integers
num1 = int(num1)
num2 = int(num2)
#now the operation
if operation == "+":
 print(" {} + {} = {}".format (num1, num2, num1 + num2 ))
elif operation == "-":
 print("{} - {} = {}".format (num1, num2, num1 - num2))
elif operation == "*":
 print("{} * {} = {}".format (num1, num2, num1 * num2))
elif operation == "**":
 print(" {} ** {} = {}".format (num1, num2, num1 ** num2))
else:
 print("x")