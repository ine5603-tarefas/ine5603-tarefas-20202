# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício Enigma
# --------------------------
# Classe que permite a criação de uma Tabela de Códigos.
#

from model.tabela_de_codigos import TabelaDeCodigos

class PainelCriaTabela:

    def crie_pre_definida(self, iu):
        print('- - - Criando Tabela de Cógidos Pré-definida - - -')
        tabela = TabelaDeCodigos()
        iu.armazene_tabela(tabela)
        print('Tabela criada!')
        input('Tecle ENTER para continuar')

    def crie_manualmente(self, iu):
        print('- - - Criando Tabela de Códigos Manualmente - - -')
        continuar = True
        caracteres = {}
        while continuar:
            caracter = input('Caracter: ')
            codigo = input('Codificar {} para: '.format(caracter))
            caracteres.update({caracter: codigo})
            continuar = 's' == input('Definir outro caracter? [s/n] ')
        tabela = TabelaDeCodigos(caracteres)
        if not tabela.valida():
            print('A tabela não é válida (há caracteres com mesmo código)')
        else:
            iu.armazene_tabela(tabela)
            print('Tabela criada!')
        input('Tecle ENTER para continuar')

