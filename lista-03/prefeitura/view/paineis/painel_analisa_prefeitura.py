# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Prefeitura
# --------------------------
# Classe que permite analisar os dados de uma prefeitura
#

from view.menu import Menu

class PainelAnalisaPrefeitura:
    def __init__(self, prefeitura):
        opcoes = {
            0: 'Voltar',
            1: 'Quantidade de Cidadãos',
            2: 'Renda Média',
            3: 'Orçamento para Renda Mínima',
            4: 'Renda Média de Faixa Etária',
            5: 'Quantidade de Idosos',
            6: 'Cidadãos com Mais Renda',
            7: 'N Cidadãos com Menos Renda'
        }
        self._prefeitura = prefeitura
        titulo = 'Analisando Prefeitura de {}'.format(prefeitura.nome())
        self._menu = Menu(titulo, opcoes)

    def analise(self):
        terminar = False
        while not terminar:
            opcao = self._menu.pergunte()
            if opcao == 0:
                terminar = True
            else:
                if opcao == 1:
                    self._mostre_qtd_cidadaos()
                elif opcao == 2:
                    self._mostre_renda_media()
                elif opcao == 3:
                    self._mostre_orcamento_renda_minima()
                elif opcao == 4:
                    self._mostre_renda_media_faixa_etaria()
                elif opcao == 5:
                    self._mostre_qtd_idosos()
                elif opcao == 6:
                    self._mostre_com_mais_renda()
                elif opcao == 7:
                    self._mostre_com_menos_renda()

    def _mostre_qtd_cidadaos(self):
        msg = 'Quantidade de cidadãos: {}'.format(self._prefeitura.qtd_cidadaos())
        print(msg)
        input('Tecle ENTER para continuar')

    def _mostre_renda_media(self):
        msg = 'Renda média (R$): {0:.2f}'.format(self._prefeitura.renda_media())
        print(msg)
        input('Tecle ENTER para continuar')

    def _mostre_orcamento_renda_minima(self):
        continuar = True
        while continuar:
            renda_minima = int(input('Qual a renda mínima desejada? '))
            (orcamento, qtd) = self._prefeitura.orcamento_renda_minima(renda_minima)
            percentual_atingido = (qtd / self._prefeitura.qtd_cidadaos()) * 100
            print('Orçamento necessário (R$): {}'.format(orcamento))
            print('Quantidade de pessoas beneficiadas: {0} ({1:.2f}%)'.format(qtd, percentual_atingido))
            continuar = 's' == input('Deseja novo cálculo? [s/n]')

    def _mostre_renda_media_faixa_etaria(self):
        continuar = True
        while continuar:
            idade_minima = int(input('Idade mínima: '))
            idade_maxima = int(input('Idade máxima: '))
            ano_atual = int(input('Ano desejado: '))
            renda_media = self._prefeitura.renda_media_de_faixa_etaria(idade_minima, idade_maxima, ano_atual)
            if renda_media is None:
                print('Nennhum cidadão encontrado para estes dados.')
            else:
                print('Renda Média (R$): {0:.2f}'.format(renda_media))
            continuar = 's' == input('Deseja novo cálculo? [s/n]')

    def _mostre_qtd_idosos(self):
        continuar = True
        while continuar:
            idade_idoso = int(input('Idade mínima para ser idoso: '))
            ano_atual = int(input('Ano desejado: '))
            qtd = self._prefeitura.qtd_idosos(idade_idoso,ano_atual)
            percentual_idosos = (qtd / self._prefeitura.qtd_cidadaos()) * 100
            print('Quantidade de idosos em {0}: {1} ({2:.2f}%)'.format(ano_atual, qtd, percentual_idosos))
            continuar = 's' == input('Deseja novo cálculo? [s/n]')

    def _mostre_com_mais_renda(self):
        continuar = True
        while continuar:
            renda = int(input('Renda: '))
            cidadaos = self._prefeitura.cidadaos_com_mais_renda_que(renda)
            percentual_cidadaos = (len(cidadaos) / self._prefeitura.qtd_cidadaos()) * 100
            print('Quantidade de cidadãos com renda superior à {0}: {1} ({2:.2f}%)'.format(renda, len(cidadaos), percentual_cidadaos))
            if 's' == input('Mostrar os cidadãos? [s/n]'):
                for c in cidadaos:
                    print(c)
            continuar = 's' == input('Deseja novo cálculo? [s/n]')

    def _mostre_com_menos_renda(self):
        continuar = True
        while continuar:
            renda = int(input('Renda: '))
            n = int(input('Quantos cidadãos encontrar: '))
            cidadaos = self._prefeitura.n_cidadaos_com_menos_renda_que(n, renda)
            percentual_cidadaos = (len(cidadaos) / self._prefeitura.qtd_cidadaos()) * 100
            print('Quantidade de cidadãos com renda inferior à {0}: {1} ({2:.2f}&)'.format(renda, len(cidadaos), percentual_cidadaos))
            if 's' == input('Mostrar os cidadãos? [s/n]'):
                for c in cidadaos:
                    print(c)
            continuar = 's' == input('Deseja novo cálculo? [s/n]')

                                