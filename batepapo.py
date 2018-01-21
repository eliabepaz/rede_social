from sistema import Sistem
sis = Sistem
class Batepapo:
    def __init__(self):
        self.conversas = list


class Conversa:
    def __init__(self):
        self.menssagens = list

class mensagem:
    def __init__(self):
        self.texto = str

    def nova_conversa(self):
        destino = input('Digite o nome do destinatario: ')
        for x in sis.contas:
            if x.nome == destino:
                txt = self.texto
                new_con = Conversa
                new_con.menssagens.append(txt)
    def nova_msg(self):
        destino = input('Digite o nome do outro prosador: ')
        new_ms = mensagem
        con = Batepapo
        for x in con.conversas:
            if x.nome == destino:
                for y in x:
                    print(y)
                new_ms.texto = input('Digite a menssagem: ')
                x.append(new_ms.texto)