class Squad:
    def __init__(self):
        self.id = ''
        self.Nome = ''
        self.Descricao = ''
        self.NumeroPessoas = 0
        self.LinguagemBackEnd = ''
        self.FrameworkFrontEnd= ''

    def __str__(self):
        return f"{self.id};{self.Nome};{self.Descricao};{self.NumeroPessoas};{self.LinguagemBackEnd};{self.FrameworkFrontEnd};"
