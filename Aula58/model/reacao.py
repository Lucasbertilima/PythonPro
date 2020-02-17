from Aula58.model.base import Base

import sqlalchemy as db


class Reacao(Base):
    __tablename__ =
    id = db.Column(db.INTEGER, primary_key=True)
    nome = db.Column(db.String)