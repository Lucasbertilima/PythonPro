# CyclicRotation
#
# Uma matriz A consistindo de N inteiros é fornecida.
# A rotação da lista significa que cada elemento é deslocado para a direita por um índice,
# e o último elemento da lista é movido para o primeiro lugar. Por exemplo, a
# rotação da lista A = [3, 8, 9, 7, 6] é[6, 3, 8, 9, 7]
# (os elementos são deslocados para a direita por um índice e 6 é movido para o primeiro lugar).
#
# O objetivo é girar a matriz A K vezes; isto é, cada elemento de A será deslocado para o K tempo certo.
#
#  Escreva uma função:
#  solução def(A, K) que, dada uma lista A que consiste em N números inteiros
# e um número inteiro K, retorna a lista A girada K vezes. Por exemplo, dado
#
# A = [3, 8, 9, 7, 6]
# K = 3
#  a função deve retornar[9, 7, 6, 3, 8].Foram realizadas três rotações:
#
# [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
# [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
# [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# Por outro exemplo, dado
#
# A = [0, 0, 0]
# K = 1
# a função deve retornar[0, 0, 0]
#
# Dado
#
# A = [1, 2, 3, 4]
# K = 4
# a
# função
# deve
# retornar[1, 2, 3, 4]


class Matriz:

    def girar(self,A,giro):
        matriz = A
        print(f'Matriz original {matriz}')
        count= 0
        while count < giro:
            matriz = matriz[1:] + matriz[:1]
            print(matriz)
            count +=1

        print(f'matriz deslocada {giro} vezes : {matriz}')




a=Matriz()
a.girar(5)