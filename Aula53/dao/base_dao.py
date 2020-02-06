import sqlalchemy as db


class BaseDao:
    def __init__(self):
        # -----database+connector://user:passwd@url:porta/database
        conexao = db.create_engine("mysql+mysqlconnector://root:@localhost:3306/aula41")
        criador_sessao = db.orm.sessionmaker()
        criador_sessao.configure(bind=conexao)
        self.sessao = criador_sessao()
