# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por obter uma cópia dos números.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import copia as faz_copia

class PainelCopia(PainelAbstrato):
    def __init__(self):
        super().__init__('Cópia')

    def interaja(self):
        numeros = self._leiaints()
        copia = faz_copia(numeros)
        msg = 'A cópia da lista {} é a lista {}.'.format(numeros, copia)
        print(msg)
