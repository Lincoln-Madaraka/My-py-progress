num1, num2, num3= input('ENTER THREE NUMBERS: ').split()
#assign the numbers to integrs
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
#add the numbers 
sum = num1 + num2 + num3
#subtract the numbers
difference = num1 - num2 - num3
#multiply the numbers
product = num1 * num2 * num3
#division
quotient = (num1 * num3) / num2 
#modulus
mod = (num1 * num3) % num2
#print the results 
print('{} + {} + {} = {}'.format(num1, num2, num3, sum))
print('{} - {} - {} = {}'.format(num1, num2, num3, difference))
print('{} * {} * {} = {}'.format(num1, num2, num3, product))
print('({} * {} / {} ) = {}'.format(num1, num3, num2, quotient))
print('({} * {}) % {} = {}'.format(num1, num3, num2, mod))