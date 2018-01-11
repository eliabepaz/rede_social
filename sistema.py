class Sistem:
    def __init__(self):
        self.shanana = None

    def menu(self):
        print('1 - Cadastrar conta')
        print('2 - Mostrar conta')
        print('x - Sair')
        opcao = input('Digite a opção:')

        if opcao == '1':
            Dado.cadastro()

        if opcao == '2':
            numero_conta = input('Conta:')
            self.mostrar_conta(numero_conta)

        return(opcao)

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
        Conts.armazenar(self.inicio)

class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None
        self.info = None


class Conts:
    def __init__(self):
        self.contas = []

    def armazenar(self, usuario):
        self.contas.append(usuario)

    def exibir_dados(self): # preparar para exibir dados
