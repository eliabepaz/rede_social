from acounts import Bd
from acounts import Conta
from acounts import Loguin
banco = Bd()
class Sistem:
    def __init__(self):
        pass
    def menu(self):
        print('1 - Cadastrar conta')
        print('2 - Loguin')
        print('x - Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1':
            usuario = Conta
            log = Loguin
            usuario.nome = input('Digite seu nome')
            usuario.idade = input('Digite sua idade')
            usuario.telefone = input('Digite seu telefone')
            usuario.endereco = input('Digite seu endereço')
            log.email = input('Digite seu email:')
            log.senha = input('Digite sua senha')
            banco.insert_user(usuario,log)
            # cria tratamento de erro para senha
        if opcao == 2:
                pass
                #fazer ligação com menu feed
        return(opcao)
