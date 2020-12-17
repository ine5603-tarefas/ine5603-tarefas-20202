# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício do Navio
# --------------------------
# Classe que representa a interface com o usuário
#

from view.menu import Menu
from view.paineis.painel_cria_navio import PainelCriaNavio
from view.paineis.painel_mostra_navio import PainelMostraNavio
from view.paineis.painel_gerencia_containers import PainelGerenciaContainer

class InterfaceComUsuario:
    def __init__(self):
        self._navio = None # inicialmente não há navio definido
        opcoes_sem_navio = {
            0: 'Sair',
            1: 'Criar Navio',
        }

        opcoes_com_navio = {
            0: 'Sair',
            1: 'Afundar Navio',
            2: 'Mostrar Navio',
            3: 'Gerenciar Containers no Navio'
        }
        self._menu_sem_navio = Menu('Programa Navio', opcoes_sem_navio)
        self._menu_com_navio = Menu('Programa Navio', opcoes_com_navio)

    def interaja(self):
        terminar = False
        while not terminar:
            if self._navio is None:
                menu = self._menu_sem_navio
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                else:
                    criador = PainelCriaNavio()
                    criador.crie(self)
            else:
                menu = self._menu_com_navio
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    self._navio = None
                elif opcao == 2:
                    painel = PainelMostraNavio()
                    painel.mostre(self._navio)
                elif opcao == 3:
                    painel = PainelGerenciaContainer()
                    painel.gerencie(self._navio)

    def armazene_navio(self, navio):
        self._navio = navio

