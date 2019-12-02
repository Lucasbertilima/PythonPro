# Aula 15 - 28-11-2019
# Manipulação de arquivos

# arquivo = open('aula.txt','x')
# arquivo.write('ssssssss\n')
# arquivo.close()

arquivo = open('aula.txt','r')
for linha in arquivo:
    print(linha)
arquivo.close()