# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício Enigma
# --------------------------
# Classe que permite codificar e decodificar frases.
#

from view.menu import Menu
from model.enigma import codifica, decodifica

class PainelEnigma:
    def __init__(self, tabela_de_codigos):
        self._tabela = tabela_de_codigos

    def interaja(self):
        opcoes = {
            0: 'Voltar',
            1: 'Codificar Frase',
            2: 'Decodificar Frase'
        }
        menu = Menu('Enigma', opcoes)
        continuar = True
        while continuar:
            opcao = menu.pergunte()
            if opcao == 0:
                continuar = False
            else:
                if opcao == 1:
                    self._codifique()
                elif opcao == 2:
                    self._decodifique()

    def _codifique(self):
        print('Caracteres válidos: {}'.format(self._tabela.caracteres()))
        frase_original = input('Digite a frase a ser codificada: ')
        frase_codificada = codifica(frase_original, self._tabela)
        if frase_codificada is None:
            print('Frase inválida! Contém pelo menos um caracter inválido')
        else:
            print('Frase codificada: {}'.format(frase_codificada))
        input('Tecle ENTER para continuar.')

    def _decodifique(self):
        print('Códigos válidos: {}'.format(self._tabela.codigos()))
        frase_codificada = input('Digite a frase a ser decodificada: ')
        frase_decodificada = decodifica(frase_codificada, self._tabela)
        if frase_decodificada is None:
            print('Frase inválida! Contém pelo menos um código inválido')
        else:
            print('Frase decodificada: {}'.format(frase_decodificada))
        input('Tecle ENTER para continuar.')

