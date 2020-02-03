import MySQLdb

from Aula41.Model.cargo_model import CargoModel

class CargoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost',database='aula41',user='root',passwd='')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM cargo")
        cargos = self.cursor.fetchall()
        lista_cargos = []
        for c in cargos:
            cargo = CargoModel(c[1],c[2],c[3],c[0])
            lista_cargos.append(cargo.__dict__)
        return lista_cargos

    def get_by_id(self,id):
        self.cursor.execute("""SELECT * FROM cargo WHERE idCargo = {}
        """.format(id))
        cargo = self.cursor.fetchone()
        cargo = CargoModel(cargo[1],cargo[2],cargo[3],cargo[0])
        return cargo.__dict__

    def insert(self,cargo:CargoModel):
        self.cursor.execute("""INSERT INTO cargo
        (Nome,Cargahoraria,salario)
        VALUES ('{}',{},{})
        """.format(cargo.nome,cargo.horas,cargo.salario))
        self.connection.commit()
        id = self.cursor.lastrowid
        cargo.id = id
        return cargo.__dict__
    def update(self,cargo:CargoModel):
        self.cursor.execute(f"""UPDATE cargo
        SET 
            Nomecargo = '{cargo.nome}'
            Cargahoraria = {cargo.horas}
            Salario = {cargo.salario}
        WHERE idCargo = {cargo.id}
        """)
        self.connection.commit()
        return cargo.__dict__

    def delete(self,id):
        self.cursor.execute(f"""DELETE FROM cargo WHERE idCargo = {id} 
        """)
        self.connection.commit()
        return F"Pessoa de id {id} foi removida"