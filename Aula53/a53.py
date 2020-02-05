#ORM
#---- SqlAlchemy
#---- pip install sqlalchemy

#---- Conector do Mysql
#---- Instalação do conector do Mysql
#---- pip install mysql-connector-python


import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class ProdutoModel(BaseModel):
    __tablename__ = 'Produto'
        id = db.column(db.INTEGER, primary_key=True )
        nome = db.column(db.String(length=100))
        descricao = db.column(db.String(length=200))

#-----database+connector://user:passwd@url:porta/database
conexao = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
criador_sessao = db.orm.session_maker()
criador_sessao.configure(bind=conexao)
sessao = criador_sessao()

produtos = sessao.query(ProdutoModel).all()

for p in produtos:
    print(p)