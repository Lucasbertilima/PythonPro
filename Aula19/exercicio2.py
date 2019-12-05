# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
def cria_lista(pess,cab):
        lista=[]
        for l in range(0,7):
                if int(pess[3][l]) >= 18:
                        dicionario={cab[0]:pess[0][l],cab[1]:pess[1][l],cab[2]:pess[2][l],cab[3]:pess[3][l]}
                        lista.append(dicionario)
        return lista


lista=cria_lista(pess,cab)



#
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())

for i in lista:
        print('{} \n'.format(i))

#
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)
for i in lista:
        print(f'{i} \n')
