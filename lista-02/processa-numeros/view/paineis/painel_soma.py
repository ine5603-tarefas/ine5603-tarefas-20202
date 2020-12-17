# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por calcular a soma dos números de uma lista.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import soma as soma_numeros

class PainelSoma(PainelAbstrato):
    def __init__(self):
        super().__init__('Soma dos Números')

    def interaja(self):
        numeros = self._leiaints()
        soma = soma_numeros(numeros)
        if soma is None:
            msg = 'Não deu para calcular pois a lista está vazia'
        else:
            msg = 'A soma da lista {} é {}'.format(numeros, soma)
        print(msg)

