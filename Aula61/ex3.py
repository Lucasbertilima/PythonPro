from collections import Counter

def solution():
    A=[1,1,1,1,1,2,2,2,2,3,3,3,3,4,5,5,5,5,6,6,6,6,7,7,7,8,8,8,9,9]


    n =Counter(A).most_common()[-1][0]
    return n

print(solution())

