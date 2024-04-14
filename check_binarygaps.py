#code calculates the binary gap of a given decimal number in binary form
def solution(N):
    if not 1 <= N <= 2_147_483_647:
        print("Error: Input must be in the range [1, 2,147,483,647]")
        return -1  

    binary_representation = bin(N)[2:]

    max_gap = 0
    current_gap = 0

    counting_zeros = False

    for digit in binary_representation:
        if digit == '1':
            if counting_zeros:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                counting_zeros = True
        elif counting_zeros:
            current_gap += 1

    return max_gap

binary_gap = eval(input("Enter a decimal number (N): "))
result = solution(binary_gap)

if result != -1:
    print(f"The binary gap of {binary_gap} is: {result}")
