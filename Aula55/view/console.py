from Aula55.dao.autor_dao import AutorDao
from Aula55.dao.pessoa_dao import PessoaDao

dao = AutorDao()
lista = dao.list_all()
for a in lista:
    print(a)