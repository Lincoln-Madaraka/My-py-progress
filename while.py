secret_number = 991

int_no = eval(input("ENTER INTEGER NUMBER: "))
while int_no != secret_number:
    print("Ha ha! You're stuck in my loop!")
while int_no == secret_number :
    print("Well done, muggle! You are free now.")
    exit(0)