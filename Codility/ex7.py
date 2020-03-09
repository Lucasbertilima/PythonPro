def solution(X,A):
    A=A
    A = [2, 2, 2, 2, 2]
    folhas=[]
    r=-1
    count = 0
    if A == []:
        return r
    for i in A:
        if i == X:
            if sum(folhas) == soma():
                return -count
            return r
            count +=1
        if folhas.count(i) >0:
            pass
        else:
            folhas.append(i)
        count += 1

def soma():
    count =9
    res = 0
    for i in range(1,count+1):
        res +=i
    return res



print(solution(2, 0))