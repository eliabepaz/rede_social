class User:
    def __init__(self):
        self.nome = ""
        self.endereco = ""
        self.data_nsc = int
        self.telefone = int

    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

    def get_endereco(self):
        return self.endereco
    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_data_nsc(self):
        return self.data_nsc
    def set_data_nsc(self, data_nsc):
        self.data_nsc = data_nsc

    def get_telefone(self):
        return self.telefone
    def set_telefone(self, telefone):
        self.telefone = telefone