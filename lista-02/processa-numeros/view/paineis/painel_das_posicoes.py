# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por obter os números em detereminadas posições.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import das_posicoes

class PainelDasPosicoes(PainelAbstrato):
    def __init__(self):
        super().__init__('Números das Posições')

    def interaja(self):
        numeros = self._leiaints('Digite a lista dos números (números separados por vírgula ou apenas enter) : ')
        posicoes = self._leiaints('Digite a lista das posições (números separados por vírgula ou apenas enter) : ')
        if not self._valide_posicoes(numeros, posicoes):
            msg = 'Há pelo menos uma posição inválida. Min: 0 Máx: {}'.format(len(numeros))
        else:
            nums_posicoes = das_posicoes(numeros, posicoes)
            msg = 'Para a lista {} e posições {} dá a lista {}.'.format(numeros, posicoes, nums_posicoes)
        print(msg)

    def _valide_posicoes(self, numeros, posicoes):
        posicoesValidas = True
        i = 0
        while posicoesValidas and i < len(posicoes):
            if posicoes[i] < 0 or posicoes[i] > len(numeros):
                posicoesValidas = False
            else:
                i += 1
        return posicoesValidas

