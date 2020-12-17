# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por verificar se lista não possui números repetidos.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import sem_repeticoes

class PainelSemRepeticoes(PainelAbstrato):
    def __init__(self):
        super().__init__('Sem Repetições')

    def interaja(self):
        numeros = self._leiaints()
        if sem_repeticoes(numeros):
            msg = 'A lista {} não possui números repetidos.'.format(numeros)
        else:
            msg = 'A lista {} possui números repetidos.'.format(numeros)
        print(msg)
