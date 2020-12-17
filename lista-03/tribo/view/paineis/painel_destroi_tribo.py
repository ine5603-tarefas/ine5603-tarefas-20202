# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Tribo
# --------------------------
# Classe responsável por destruir uma tribo
#

from view.paineis.painel_abstrato import PainelAbstrato

class PainelDestroiTribo(PainelAbstrato):
    def __init__(self, iu, tribo):
        super().__init__('Destruir Tribo {}'.format(tribo.nome()), iu)
        self._tribo = tribo

    def _interaja(self):
        if 's' == input('Deseja mesmo destruir? [s/n] '):
            self._iu.armazene_tribo(None)
            print('Tribo destruída!')