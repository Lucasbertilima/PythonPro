def solution(X,A):
    A=A
    A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    if X not in A:
        return -1
    count = 0
    for i in A:
        if X == i :
            return count
        else:
            count +=1

print(solution(3,0))