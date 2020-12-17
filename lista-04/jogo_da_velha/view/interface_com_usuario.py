# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Jogo da Velha
# --------------------------
# Classe que representa a interface com o usuário
#

from view.menu import Menu
from view.paineis.painel_cria_jogo import PainelCriaJogo
from view.paineis.painel_gerencia_partida import PainelGerenciaPartida

class InterfaceComUsuario:
    def __init__(self):
        self._jogo = None # inicialmente não há jogo definido
        opcoes_sem_jogo = {
            0: 'Sair',
            1: 'Criar Jogo'
        }

        opcoes_com_jogo = {
            0: 'Sair',
            1: 'Destruir Jogo',
            2: 'Iniciar Partida'
        }
        self._menu_sem_jogo = Menu('Programa Jogo da Velha', opcoes_sem_jogo)
        self._menu_com_jogo = Menu('Programa Jogo da Velha', opcoes_com_jogo)

    def interaja(self):
        terminar = False
        while not terminar:
            if self._jogo is None:
                menu = self._menu_sem_jogo
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    criador = PainelCriaJogo()
                    criador.crie(self)
            else:
                menu = self._menu_com_jogo
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    self._jogo = None
                elif opcao == 2:
                    painel = PainelGerenciaPartida()
                    painel.gerencie(self, self._jogo)

    def armazene_jogo(self, jogo):
        self._jogo = jogo
