# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por encontrar o primeiro e o último número.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import primeiro_e_ultimo

class PainelPrimeiroEUltimo(PainelAbstrato):
    def __init__(self):
        super().__init__('Primeiro e Último')

    def interaja(self):
        numeros = self._leiaints()
        resposta = primeiro_e_ultimo(numeros)
        if resposta is None:
            msg = 'Não dá para encontrar porque a lista {} tem menos de 2 números'.format(numeros)
        else:
            msg = 'Para a lista {} o primeiro é o {} e último é o {}'.format(numeros, resposta[0], resposta[1])
        print(msg)
