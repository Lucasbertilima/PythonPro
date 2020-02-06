from Aula53.model.cargo_model import CargoModel
from Aula53.dao.base_dao import BaseDao


class CargoDao(BaseDao):

    def list_all(self):
        return self.sessao.query(CargoModel).all()

    def get_by_id(self,id):
        return  self.sessao.query(CargoModel).filter_by(idcargo=id).first()

    def insert(self, cargo:CargoModel):
        self.sessao.add(cargo)
        self.sessao.commit()
        return self.sessao.query(CargoModel).all()

    def update(self):
        a = self.sessao.query(CargoModel)
        a = a.filter(CargoModel.idcargo==3)
        cargo = a.one()
        cargo.Nomecargo = 'programmer'
        self.sessao.commit()

    def delete(self,id):
        a = self.sessao.query(CargoModel).filter_by(idcargo=id).first()
        self.sessao.delete(a)
        self.sessao.commit()
