num1, num2 = input('ENTER TWO NUMBERS: ').split()
#assign the numbers
num1 = int(num1)
num2 = int(num2)
#add the numbers 
sum = num1 + num2
#subtract the numbers
difference = num1 - num2
#multiply the numbers
product = num1 * num2
#division
quotient = num1 / num2
#modulus
mod = num1 % num2
#print the results 
print('{} + {} = {}'.format(num1, num2, sum))
print('{} - {} = {}'.format(num1, num2, difference))
print('{} * {} = {}'.format(num1, num2, product))
print('{} / {} = {}'.format(num1, num2, quotient))
print('{} % {} = {}'.format(num1, num2, mod))