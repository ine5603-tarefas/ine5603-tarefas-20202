# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício da Prefeitura
# --------------------------
# Classe responsável por descobrir o que o usuário deseja fazer.

class Menu:
    def __init__(self, titulo, opcoes):
        self._titulo = titulo
        self._opcoes = opcoes

    def pergunte(self):
        self._mostre()
        return self._leia_opcao()

    def _mostre(self):
        msg_titulo = '==== {}'.format(self._titulo)
        print(msg_titulo)
        for (k,v) in self._opcoes.items():
            print('[{}] {}'.format(k,v))
        print('====')

    def _leia_opcao(self):
        op = self._leia_inteiro('Digite sua opção : ')
        while op not in self._opcoes:
            print('Opção inválida!')
            op = self._leia_inteiro('Digite sua opção : ')
        return op

    def _leia_inteiro(self, msg):
        numero = -1
        while numero < 0:
            try:
                numero = int(input(msg))
                if numero < 0:
                    print('O número tem que ser maior ou igual a zero!')
            except ValueError:
                print('Erro! Digite um número inteiro maior ou igual a zero.')
        return numero
