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

 #this code had refused to work at first and my editor couldnt see the err
 #i learnt after a while my error was the whitespaces when declaring operations
 #operation == "-", no spaces around the sign