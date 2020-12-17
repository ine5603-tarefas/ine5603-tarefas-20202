# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Balde
# --------------------------
# Classe que permite que os baldes seja criados.
#

from model.balde import Balde

class PainelCriaBaldes:
    def crie(self, iu):
        print('--- Criar Dois Baldes ---')
        capA = int(input('Qual a capacidade do balde A? '))
        capB = int(input('Qual a capacidade do balde B? '))
        baldeA = Balde(capA)
        baldeB = Balde(capB)
        iu.armazene_baldes(baldeA, baldeB)