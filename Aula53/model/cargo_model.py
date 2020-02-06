import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class CargoModel(BaseModel):
    __tablename__ = "cargo"
    idcargo= db.Column(db.INTEGER, primary_key=True)
    Nomecargo = db.Column(db.String(length=100))
    Cargahoraria = db.Column(db.INTEGER)
    Salario = db.Column(db.FLOAT)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.idcargo, self.Nomecargo, self.Cargahoraria, self.Salario)

    def __repr__(self):
        return self.__str__()
