class Sistem:
    def __init__(self):
        self.shanana = None

    def menu(self, op):
        print('1 - Fazer Cadastro: ')
        opcao = input('Digite o numero da ação desejada: ')
        if opcao == '1':
            Dado.cadastro()
            return(opcao)
        return(opcao)

#substituir menu

class Dado:
    def __init__(self, nome, endereco, data_nsc, telefone, email, senha):
        self.nome = nome
        self.endereco = endereco
        self.data_nsc = data_nsc
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.defalt_dados = []
        self.loguin_dados = []
    def cadastro(self):
        self.nome = input(str('Digite seu nome: '))
        self.defalt_dados.append(self.nome)
        self.endereco = input(str('Digite seu endereço: '))
        self.defalt_dados.append(self.endereco)
        self.data_nsc = input(str('Digite sua data de nascimento: '))
        self.defalt_dados.append(self.data_nsc)
        self.telefone = input(str('Digite seu telefone: '))
        self.defalt_dados.append(self.telefone)
        self.email = input(str('Digite um email valido: '))
        self.loguin_dados.append(self.email)
        self.senha = input(str('Digite uma senha: '))
        self.loguin_dados.append(self.senha)
        User.start(self.defalt_dados, self.loguin_dados)

class User:
    def __init__(self):
        self.num_user = 0
    def id(self):
        self.num_user += 1
    def start(self , l_defalt, l_loguin):
        i_name = self.num_user
        Lista_Encadeada.inserir_dados(i_name, l_defalt, l_loguin)
        self.id()


class Lista_Encadeada:
    def __init__(self):
        self.inicio = None

    def inserir_dados(self, name, dados, log):
        novo_no = No(name)
        novo_no.proximo = self.inicio
        self.inicio = novo_no
        self.inicio.info = dados
        self.log = log


class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None
        self.info = None