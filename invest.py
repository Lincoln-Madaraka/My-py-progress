#user enters their investment amount and expected cumulative amount and profit
#interest * investment + total
inpt_amount = input("ENTER INIIAL AMOUNT: ")
inpt_amount = float(inpt_amount)
output_amnt = input ("ENTER EXPECTED OUTPUT AMOUNT: ")
output_amnt = float(output_amnt)
print("For input amount {} we expect ouput amount {:.2f}".format (inpt_amount, output_amnt))
#for expected output
for i in range (1):
    output_amnt = output_amnt * 1000 + inpt_amount
    print("The output we get here is:  ", output_amnt)