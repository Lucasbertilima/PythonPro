import MySQLdb
#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM endereco')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)
        
#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM endereco WHERE idEndereco = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, Logradouro):
    c.execute(f"SELECT * FROM endereco WHERE Logradouro like '{Logradouro}%' ")
    for p  in  c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr,idEndereco, Logradouro, Numero, Complemento, Bairro):
    cr.execute(f"INSERT INTO endereco (idEndereco,Logradouro,Numero,Complemento,Bairro )VALUES({idEndereco},'{Logradouro}', '{Numero}','{Complemento}','{Bairro}')")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id, Logradouro,Numero,Complemento,Bairro):
    cr.execute(f"UPDATE endereco SET Logradouro='{Logradouro}', Numero='{Numero}', Complemento='{Complemento}', Bairro='{Bairro}' WHERE idEndereco={id} ")
    cn.commit()

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM endereco WHERE idEndereco={id}')
    cn.commit()

conexao = MySQLdb.connect(host='localhost', database='aulabd', user = 'root', passwd = '')
cursor = conexao.cursor()

# listar_todos(cursor)
# buscar_por_id(cursor, 2)
# buscar_por_sobrenome(cursor,'Ru')
# salvar(conexao, cursor,3, '2 de Novembro', '989', 'Ao lado ','Velha')
# alterar(conexao, cursor, 3, 'goiaba', 'doce', 'Perto', 'Garcia')
deletar(conexao, cursor, 3)