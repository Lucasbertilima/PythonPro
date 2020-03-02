from collections import Counter

def solution():
    A=[1,5,1,5,3,5]
    A.sort()
    if len(A) == 1:
        return A[0]

    size = len(A)
    for i in range(0, size, 2):
        if i == size - 1:
            return A[i]
        if A[i] != A[i + 1]:
            return A[i]

print(solution())

