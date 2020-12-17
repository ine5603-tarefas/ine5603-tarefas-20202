# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Balde
# --------------------------
# Classe que representa a interface com o usuário
#

from view.menu import Menu
from view.paineis.painel_cria_baldes import PainelCriaBaldes
from view.paineis.painel_destroi_baldes import PainelDestroiBaldes
from view.paineis.painel_manipula_baldes import PainelManipulaBaldes

class InterfaceComUsuario:
    def __init__(self):
        self._baldes = None # inicialmente não há baldes definidos
        opcoes_sem_balde = {
            0: 'Sair',
            1: 'Criar Baldes'
        }
        opcoes_com_balde = {
            0: 'Sair',
            1: 'Destruir Baldes',
            2: 'Manipular Baldes'
        }
        self._menu_sem_baldes = Menu('Programa Baldes', opcoes_sem_balde)
        self._menu_com_baldes = Menu('Programa Baldes', opcoes_com_balde)

    def interaja(self):
        terminar = False
        while not terminar:
            if self._baldes is None:
                menu = self._menu_sem_baldes
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    criador = PainelCriaBaldes()
                    criador.crie(self)
            else:
                menu = self._menu_com_baldes
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    destruidor = PainelDestroiBaldes()
                    destruidor.destrua(self)
                elif opcao == 2:
                    manipulador = PainelManipulaBaldes()
                    manipulador.manipule(self._baldes[0], self._baldes[1])

    def armazene_baldes(self, baldeA, baldeB):
        self._baldes = (baldeA, baldeB)

    def destrua_baldes(self):
        self._baldes = None

