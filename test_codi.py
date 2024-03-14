def solution(A):
    A.sort()
    smallest_positive = 1

    for num in A:
        if num == smallest_positive:
            smallest_positive += 1

    return smallest_positive

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
