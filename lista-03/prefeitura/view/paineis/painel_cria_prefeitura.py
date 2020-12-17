# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Prefeitura
# --------------------------
# Classe que permite a criação de uma prefeitura
#

from model.gera_populacao import gera_populacao_aleatoria, gera_populacao_fixa
from model.prefeitura import Prefeitura
from model.cidadao import Cidadao

class PainelCriaPrefeitura:

    def crie_aleatorio(self, iu):
        print('- - - Criar Prefeitura Com Dados Aleatórios - - -')
        nome = input('Qual é o nome do município? ')
        num_cidadaos = int(input('Quantos cidadãos? '))
        print('Gerando {} cidadãos.'.format(num_cidadaos))
        populacao = gera_populacao_aleatoria(qtd=num_cidadaos)
        print('Pronto!')
        prefeitura = Prefeitura(nome, populacao)
        input('Tecle ENTER para continar')
        iu.armazene_prefeitura(prefeitura)

    def crie_fixo(self, iu):
        print('- - - Criar Prefeitura Com Dados Fixos - - -')
        nome = input('Qual é o nome do município? ')
        populacao = gera_populacao_fixa()
        prefeitura = Prefeitura(nome, populacao)
        input('Tecle ENTER para continar')
        iu.armazene_prefeitura(prefeitura)

    def crie_digitado(self, iu):
        print('- - - Criar Prefeitura Com Dados Digitados - - -')
        nome = input('Qual é o nome do município? ')
        print('** Definir Cidadãos **')
        continuar = True
        populacao = []
        while continuar:
            ano = int(input('Ano de nascimento: '))
            renda = int(input('Renda (R$): '))
            populacao.append(Cidadao(ano, renda))
            continuar = 's' == input('Informar outro cidadão? [s/n]')
        prefeitura = Prefeitura(nome, populacao)
        input('Tecle ENTER para continar')
        iu.armazene_prefeitura(prefeitura)