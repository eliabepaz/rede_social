class User:

    def __init__(self):
        self.nome = str
        self.endereco = str
        self.data_nsc = int
        self.telefone = int
        self.email = str
        self.senha = str


    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_endereco(self):
        return self.endereco
    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def get_data_nsc(self):
        return self.data_nsc
    def set_data_nsc(self, novo_data_nsc):
        self.data_nsc = novo_data_nsc

    def get_telefone(self):
        return self.telefone
    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def set_email(self,novo_email):
        self.email = novo_email
    def set_senha(self, nova_senha):
        self.senha = nova_senha

    def logar(self):
        resposta = str
        while(resposta != 'loguin efetuado'):
            e = input("Insira o email:")
            s = input ("Senha:")
            if e == self.email and s == self.senha:
                print('Loguin efetuado' )
            else:
                print('email ou senha incorretos')
                respoata = ('email ou senha incorretos')
