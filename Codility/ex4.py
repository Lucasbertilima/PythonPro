def solution(X,Y,D):
    while True:
        if X >= Y:
            break
        else:
            distancia = Y-X
            obtida = distancia/D
            break



    print(int(obtida))

# print(solution(10,10,20))
solution(10,100,2)