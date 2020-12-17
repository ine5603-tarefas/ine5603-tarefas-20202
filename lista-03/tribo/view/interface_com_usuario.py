# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Tribo
# --------------------------
# Classe que representa a interface com o usuário
#

from view.menu import Menu
from view.paineis.painel_cria_tribo import PainelCriaTribo
from view.paineis.painel_destroi_tribo import PainelDestroiTribo
from view.paineis.painel_gerencia_tribo import PainelGerenciaTribo


class InterfaceComUsuario:
    def __init__(self):
        self._tribo = None  # inicialmente não há tribo definida
        opcoes_sem_tribo = {
            0: 'Sair',
            1: 'Criar Tribo',
        }
        opcoes_com_tribo = {
            0: 'Sair',
            1: 'Destruir Tribo',
            2: 'Gerenciar Tribo'
        }
        self._menu_sem_tribo = Menu('Programa Tribo', opcoes_sem_tribo)
        self._menu_com_tribo = Menu('Programa Tribo', opcoes_com_tribo)

    def interaja(self):
        terminar = False
        while not terminar:
            painel = self._defina_painel()
            if painel is None:
                terminar = True
            else:
                painel.interaja()

    def _defina_painel(self):
        painel = None
        if self._tribo is None:
            opcao = self._menu_sem_tribo.pergunte()
            if opcao == 1:
                painel = PainelCriaTribo(self)
        else:
            opcao = self._menu_com_tribo.pergunte()
            if opcao == 1:
                painel = PainelDestroiTribo(self, self._tribo)
            elif opcao == 2:
                painel = PainelGerenciaTribo(self, self._tribo)
        return painel

    def armazene_tribo(self, tribo):
        self._tribo = tribo
