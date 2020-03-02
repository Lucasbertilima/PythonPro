def solution(A):
    A = A
    h = A[0]
    c = sum(A[1:])
    min_dif = float('inf')
    for i in
        h += A[i]
        c -= A[i]
        if abs(h - c) < min_dif:
            min_dif = abs(h - c)

        return min_dif


solution([3,1,2,4,3])