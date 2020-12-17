# -------------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Matriz de Inteiros
# -------------------------------
# Classe que representa a interface com o usuário
#

from view.menu import Menu
from view.paineis.painel_cria_matriz import PainelCriaMatriz
from view.paineis.painel_povoa_matriz import PainelPovoaMatriz
from view.paineis.painel_soma_matrizes import PainelSomaMatrizes
from view.paineis.painel_multiplica_matrizes import PainelMultiplicaMatrizes
from view.paineis.painel_analisa_matriz import PainelAnalisaMatriz

class InterfaceComUsuario:
    def __init__(self):
        self._matrizes = {'A': None, 'B': None} # inicialmente não há matrizes definidas
        opcoes_sem_matrizes = {
            0: 'Sair',
            1: 'Criar Matriz A',
            2: 'Criar Matriz B',
        }

        opcoes_com_matrizes = {
            0: 'Sair',
            1: 'Destruir Matriz A',
            2: 'Destruir Matriz B',
            3: 'Povoar Matriz A',
            4: 'Povoar Matriz B',
            5: 'Somar Matrizes A e B',
            6: 'Multiplicar Matrizes A e B',
            7: 'Analisar Matriz'
        }
        self._menu_sem_matrizes = Menu('Programa Matriz de Inteiros', opcoes_sem_matrizes)
        self._menu_com_matrizes = Menu('Programa Matriz de Inteiros', opcoes_com_matrizes)

    def interaja(self):
        terminar = False
        while not terminar:
            if self._matrizes['A'] is None or self._matrizes['B'] is None:
                menu = self._menu_sem_matrizes
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    criador = PainelCriaMatriz()
                    criador.crie(self, 'A')
                elif opcao == 2:
                    criador = PainelCriaMatriz()
                    criador.crie(self, 'B')
            else:
                menu = self._menu_com_matrizes
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    self._matrizes['A'] = None
                elif opcao == 2:
                    self._matrizes['B'] = None
                elif opcao == 3:
                    povoador = PainelPovoaMatriz()
                    povoador.povoe('A', self._matrizes['A'])
                elif opcao == 4:
                    povoador = PainelPovoaMatriz()
                    povoador.povoe('B', self._matrizes['B'])
                elif opcao == 5:
                    somador = PainelSomaMatrizes()
                    somador.some('A', self._matrizes['A'], 'B', self._matrizes['B'])
                elif opcao == 6:
                    multiplicador = PainelMultiplicaMatrizes()
                    multiplicador.multiplique('A', self._matrizes['A'], 'B', self._matrizes['B'])
                elif opcao == 7:
                    analisador = PainelAnalisaMatriz()
                    analisador.analise(self._matrizes)

    def armazene_matriz(self, nome, matriz):
        self._matrizes[nome] = matriz
