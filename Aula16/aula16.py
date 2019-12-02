# Aula 16 - 29-11-2019
# 

from faixa import salvar, salvar_faixa , ler_faixa

# Cadastro de playlist
# Lendo musica,artista e album

musica = input('Digite uma musica')
artista = input('Digite o nome do artista')
album = input('Digite o nome do album')

faixa = salvar(musica,album,artista)
salvar_faixa(faixa) 
lista=ler_faixa(faixa)
for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["artista"]} - {faixa["album"]}')
    
