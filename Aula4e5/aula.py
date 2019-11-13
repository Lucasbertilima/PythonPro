#Aula 4 11-11-2019                                                                                                
# Estrutura de decisão                                                                                                
        
idade = 18                                                                                               
#---- if simples, validação de apenas uma condição                                                                                                
if idade ==18:                                                                                                
    print('Maior')                                                                                                
        
#--- if com else                                                                                                
#--- caso a condição validada pelo if não seja verdadeira,                                                                                                 
#--- O Else é executado                                                                                                
if idade<18:                                                                                                
    print('Menor')                                                                                                
else:                                                                                                
    print('Maior')                                                                                                
        
#--- if com Elif e else                                                                                                 
#--- Caso a condição validade no if seja falsa                                                                                                
#--- É validado a condição do Elif                                                                                                
#--- Caso a condição do Elif seja falsa                                                                                                 
#--- Else é executado                                                                                                
if idade>18:                                                                                                
    print('Dimenor')                                                                                                
elif idade == 18:                                                                                                
    print('Silasco')                  
else:                                                                                                
    print('SilascoMaisAinda')                                                                                                
        
#--- if com variável booleana, não é necessário a validação(==True)                                                                                                
#--- Se a variável for verdadeira, o usuario loga, caso contrario é negado                                                                                               
#--- No caso da variável bool, não é necessária a validação                                                                                                 
ativo = True                                                                                                 
if ativo :                                                                                                
    print('Logar')                                                                                                
else:                                                                                                
    print('Não pode')   
                                                                                             