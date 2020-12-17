# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Prefeitura
# --------------------------
# Classe que representa a interface com o usuário
#

from view.menu import Menu
from view.paineis.painel_cria_prefeitura import PainelCriaPrefeitura
from view.paineis.painel_analisa_prefeitura import PainelAnalisaPrefeitura

class InterfaceComUsuario:
    def __init__(self):
        self._prefeitura = None # inicialmente não há prefeitura definida
        opcoes_sem_prefeitura = {
            0: 'Sair',
            1: 'Criar Prefeitura com Dados Aleatórios',
            2: 'Criar Prefeitura com Dados Digitados',
            3: 'Criar Prefeitura com Dados Fixos'
        }

        opcoes_com_prefeitura = {
            0: 'Sair',
            1: 'Destruir Prefeitura',
            2: 'Analisar Prefeitura'
        }
        self._menu_sem_prefeitura = Menu('Programa Prefeitura', opcoes_sem_prefeitura)
        self._menu_com_prefeitura = Menu('Programa Prefeitura', opcoes_com_prefeitura)

    def interaja(self):
        terminar = False
        while not terminar:
            if self._prefeitura is None:
                menu = self._menu_sem_prefeitura
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    criador = PainelCriaPrefeitura()
                    criador.crie_aleatorio(self)
                elif opcao == 2:
                    criador = PainelCriaPrefeitura()
                    criador.crie_digitado(self)
                elif opcao == 3:
                    criador = PainelCriaPrefeitura()
                    criador.crie_fixo(self)
            else:
                menu = self._menu_com_prefeitura
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    self._prefeitura = None
                elif opcao == 2:
                    analisador = PainelAnalisaPrefeitura(self._prefeitura)
                    analisador.analise()

    def armazene_prefeitura(self, prefeitura):
        self._prefeitura = prefeitura
