# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Tribo
# --------------------------
# Classe responsável por criar uma tribo
#

from model.tribo import Tribo
from view.paineis.painel_abstrato import PainelAbstrato

class PainelCriaTribo(PainelAbstrato):

    def __init__(self, iu):
        super().__init__('Criar Tribo', iu)

    def _interaja(self):
        nome = input('Nome da tribo: ')
        qtd_guerreiros = int(input('Quantidade máxima de guerreiros: '))
        qtd_vidas = int(input('Quantidade máxima de vidas de cada guerreiro: '))
        tribo = Tribo(nome, qtd_guerreiros, qtd_vidas)
        self._iu.armazene_tribo(tribo)
        print('Tribo criada!')
