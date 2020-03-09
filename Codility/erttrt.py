lista = [1,2,3,4,5,6,7,8,9]

def soma():
    count =9
    res = 0
    for i in range(1,count+1):
        res +=i
    return res

a = soma()
print(a)
print(sum(lista))