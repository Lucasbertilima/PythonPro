import MySQLdb
#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM pessoa')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)
        
#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM pessoa WHERE idPessoa = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM pessoa WHERE Sobrenome like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr,idpessoa, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO pessoa (idPessoa,Nome, Sobrenome, Idade, enderecoid )VALUES({idpessoa},'{nome}', '{sobrenome}',{idade},{endereco_id})")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"UPDATE pessoa SET Nome='{nome}', Sobrenome='{sobrenome}', Idade={idade}, enderecoid={endereco_id} WHERE idPessoa={id} ")
    cn.commit()

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM pessoa WHERE idPessoa={id}')
    cn.commit()

conexao = MySQLdb.connect(host='localhost', database='aulabd', user = 'root', passwd = '')
cursor = conexao.cursor()

# listar_todos(cursor)
# buscar_por_id(cursor, 2)
# buscar_por_sobrenome(cursor,'li')
# salvar(conexao, cursor,4, 'py', 'charm', 8,2)
# alterar(conexao, cursor, 0, 'goiaba', 'doce', 32, 1)
deletar(conexao, cursor, 0)