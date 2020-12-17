# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por obter unir duas listas de números.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import una

class PainelUna(PainelAbstrato):
    def __init__(self):
        super().__init__('Unir Listas')

    def interaja(self):
        numeros1 = self._leiaints('Digite a primeira lista (números separados por vírgula ou apenas enter) : ')
        numeros2 = self._leiaints('Digite a segunda lista (números separados por vírgula ou apenas enter) : ')
        unidos = una(numeros1, numeros2)
        msg = 'Unindo {} com {} dá {}.'.format(numeros1, numeros2, unidos)
        print(msg)
