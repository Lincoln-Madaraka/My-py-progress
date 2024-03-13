def solution(N):
    if not 1 <= N <= 2147483647:
        print("ERROR!! Value must be within range [1,..2,171,483,647]")
        return -1
     
    binary_representation = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    for digit in binary_representation:
        if digit == '0':
            current_gap += 1
        else:
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        return max_gap
binary_gap = eval(input("ENTER DECIMAL NUMBER: "))
result = solution(binary_gap)
if result != -1:
    print(f"The binary gap of {binary_gap} is: {result}")
