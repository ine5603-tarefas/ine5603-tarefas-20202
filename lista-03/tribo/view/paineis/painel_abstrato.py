# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Tribo
# --------------------------
# Classe responsável por definir um painel abstrato
#

from abc import ABC, abstractmethod

class PainelAbstrato(ABC):

    def __init__(self, titulo, iu):
        self._titulo = titulo
        self._iu = iu
        self._continua = True

    def interaja(self):
        print('- - - {} - - - '.format(self._titulo))
        self._interaja()
        if self._continua:
            input('Tecle ENTER para continuar')

    def _nao_continue(self):
        self._continua = False

    @abstractmethod
    def _interaja(self):
        pass