def solution(N):
    Binario = bin(int(N))[2:]
    Binario = Binario.split('1')
    Binario.pop()
    return len(max(Binario))



print(solution(15))