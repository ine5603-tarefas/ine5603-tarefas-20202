# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Relógio
# --------------------------
# Classe que representa a interface com o usuário
#

from view.menu import Menu
from view.paineis.painel_cria_relogio import PainelCriaRelogio
from view.paineis.painel_manipula_relogio import PainelManipulaRelogio
from view.paineis.painel_compara_relogios import PainelComparaRelogios

class InterfaceComUsuario:
    def __init__(self):
        self._relogio = None # inicialmente não há relógio definido
        opcoes_sem_relogio = {
            0: 'Sair',
            1: 'Criar Relógio Marcando 00:00:00',
            2: 'Criar Relógio Marcando hh:00:00',
            3: 'Criar Relógio Marcando 00:mm:00',
            4: 'Criar Relógio Marcando 00:00:ss',
            5: 'Criar Relógio Marcando hh:mm:00',
            6: 'Criar Relógio Marcando 00:mm:ss',
            7: 'Criar Relógio Marcando hh:00:ss',
            8: 'Criar Relógio Marcando hh:mm:ss'
        }

        opcoes_com_relogio = {
            0: 'Sair',
            1: 'Destruir Relógio',
            2: 'Manipular Relógio',
            3: 'Comparar Relógios'
        }
        self._menu_sem_relogio = Menu('Programa Relógio', opcoes_sem_relogio)
        self._menu_com_relogio = Menu('Programa Relógio', opcoes_com_relogio)

    def interaja(self):
        op_tipo = {1 : '', 2: 'h', 3: 'm', 4: 's', 5: 'hm', 6: 'ms', 7: 'hs', 8: 'hms'}
        terminar = False
        while not terminar:
            if self._relogio is None:
                menu = self._menu_sem_relogio
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                else:
                    criador = PainelCriaRelogio()
                    criador.crie(op_tipo[opcao], self)
            else:
                menu = self._menu_com_relogio
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    self._relogio = None
                elif opcao == 2:
                    manipulador = PainelManipulaRelogio()
                    manipulador.manipule(self._relogio)
                elif opcao == 3:
                    comparador = PainelComparaRelogios()
                    comparador.compare(self._relogio)

    def armazene_relogio(self, relogio):
        self._relogio = relogio
