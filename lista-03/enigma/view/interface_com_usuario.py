# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício Enigma
# --------------------------
# Classe que representa a interface com o usuário
#

from view.menu import Menu
from view.paineis.painel_cria_tabela import PainelCriaTabela
from view.paineis.painel_enigma import PainelEnigma

class InterfaceComUsuario:
    def __init__(self):
        self._tabela_de_codigos = None # inicialmente não há tabela definida
        opcoes_sem_tabela = {
            0: 'Sair',
            1: 'Criar Tabela de Códigos Pré-definida',
            2: 'Criar Tabela de Códigos Manualmente',
        }

        opcoes_com_tabela = {
            0: 'Sair',
            1: 'Destruir Tabela de Códigos',
            2: 'Enigma: Codificar/Decodificar Frase'
        }
        self._menu_sem_tabela = Menu('Programa Enigma', opcoes_sem_tabela)
        self._menu_com_tabela = Menu('Programa Enigma', opcoes_com_tabela)

    def interaja(self):
        terminar = False
        while not terminar:
            if self._tabela_de_codigos is None:
                menu = self._menu_sem_tabela
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    criador = PainelCriaTabela()
                    criador.crie_pre_definida(self)
                elif opcao == 2:
                    criador = PainelCriaTabela()
                    criador.crie_manualmente(self)
            else:
                menu = self._menu_com_tabela
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    self._tabela_de_codigos = None
                elif opcao == 2:
                    analisador = PainelEnigma(self._tabela_de_codigos)
                    analisador.interaja()

    def armazene_tabela(self, tabela_de_codificacao):
        self._tabela_de_codigos = tabela_de_codificacao
