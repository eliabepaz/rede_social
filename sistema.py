from acounts import Loguin
from BD import log
from acounts import Dados
conta = Dados
log_dados = Loguin
log_list = log

class Sistem:
    def __init__(self):
        self.identificador = None

    def menu(self):
        print('1 - Cadastrar conta')
        print('2 - Mostrar conta')
        print('3 - Cadastrar Email e Senha')
        print('x - Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1':
            print('\n\n\n')
            conta.nome = input('Digite seu nome: ')
            conta.idade = input('Digite sua idade: ')
            conta.telefone = input('Digite seu telefone: ')
            conta.endereco = input('Digite seu endereço: ')
            print('\n\n\n')
        if opcao == '2':
            print('Nome do usuario: ' + str(conta.nome) + '\nIdade: ' + str(conta.idade) + '\nTelefone: ' + str(conta.telefone) + '\nEndereço: ' + str(conta.endereco))

        if opcao == '3':
            log_dados.email = input('Digite um email valido:')
            log_dados.senha = input('Digite um senha:')
            log_list.emails.append(log_dados.email)
            log_list.senhas.append(log_dados.senha)
        return(opcao)
