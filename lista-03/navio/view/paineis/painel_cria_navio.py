# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício do Navio
# --------------------------
# Classe que permite que um navio seja criado
#

from model.navio import Navio

class PainelCriaNavio:

    def crie(self, iu):
        print('- - - Criar Navio - - - ')
        num_containers = int(input('Quantos containers cabem no navio? '))
        peso_maximo = int(input('Qual o peso máximo que o navio consegue transportar? '))
        navio = Navio(num_containers, peso_maximo)
        iu.armazene_navio(navio)