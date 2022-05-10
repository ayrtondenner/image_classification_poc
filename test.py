def solution(A):
    # write your code in Python 3.6
    A = set(A)

    A = [number for number in A if number > 0]
    A.sort()

    if len(A) == 0 or A[0] > 1:
        return 1

    last_right_index = None

    for index, number in enumerate(A):
        if index + 1 != number:
            break

        last_right_index = index

    return A[last_right_index] + 1


listas = [[1, 3, 6, 4, 1, 2], [1, 2, 3], [-1, -3], [-1, 2], [-2, -3, 1, 2, 4], [-2, -1, 0, 2, 3, 4, 5]]

for lista in listas:

    print(solution(lista))