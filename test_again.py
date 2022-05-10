def solution(A):
    # write your code in Python 3.6

    A = set(A)

    A = [number for number in A if number > 0]

    if len(A) == 0:
        return 1

    A.sort()

    for index, number in enumerate(A):
        if number != index + 1:
            return index + 1 # - 1 + 2

    return len(A) + 1


list_test = [
    [1, 3, 6, 4, 1, 2],
    [1, 2, 3],
    [-1, -3],
    [-2, -3, 1, 2, 4],
    [-2, -1, 0, 2, 3, 4, 5]
]

for test in list_test:
    print(solution(test))