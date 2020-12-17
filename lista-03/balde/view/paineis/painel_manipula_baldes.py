# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Balde
# --------------------------
# Classe que permite manipular os baldes.
#

from view.menu import Menu
from model.balde import Balde

class PainelManipulaBaldes:
    def __init__(self):
        opcoes = {
            0: 'Voltar',
            1 : 'Encher balde A',
            2 : 'Encher balde B',
            3 : 'Esvaziar balde A',
            4 : 'Esvaziar balde B',
            5 : 'Derrame balde A em balde B',
            6 : 'Derrame balde B em balde A',
            7 : 'Balde A receba de balde B',
            8 : 'Balde B receba de balde A'
        }
        self._menu = Menu('Opções de Manipulação', opcoes)

    def manipule(self, baldeA, baldeB):
        print('--- Manipula Baldes ---')
        encerrar = False
        while not encerrar:
            self._mostre_baldes(baldeA, baldeB)
            opcao = self._menu.pergunte()
            if opcao == 0:
                encerrar = True
            elif opcao == 1:
                baldeA.fique_cheio()
            elif opcao == 2:
                baldeB.fique_cheio()
            elif opcao == 3:
                baldeA.fique_vazio()
            elif opcao == 4:
                baldeB.fique_vazio()
            elif opcao == 5:
                baldeA.derrame_em(baldeB)
            elif opcao == 6:
                baldeB.derrame_em(baldeA)
            elif opcao == 7:
                baldeA.receba_de(baldeB)
            elif opcao == 8:
                baldeB.receba_de(baldeA)

    def _mostre_baldes(self, baldeA, baldeB):
        print('****** Situação Atual dos Baldes')
        print('- Balde A')
        self._mostre_balde(baldeA)
        print('- Balde B')
        self._mostre_balde(baldeB)
        print('****************************\n')

    def _mostre_balde(self, balde):
        print('capacidade : {}'.format(balde.capacidade()))
        print('quantidade : {}'.format(balde.quantidade()))
        print('está cheio : {}'.format(balde.esta_cheio()))
        print('está vazio : {}'.format(balde.esta_vazio()))
