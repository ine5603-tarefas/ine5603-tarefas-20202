# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício da Prefeitura
# --------------------------
# Classe responsável por representar uma prefeitura.

from model.cidadao import Cidadao

class Prefeitura:
    def __init__(self, nome, cidadaos):
        '''Uma prefeitura é caracterizada pelo seu nome e por
        uma lista de cidadãos (objetos da classe Cidadao) cadastrados.
        '''
        self._nome = nome
        self._cidadaos = cidadaos
        
    def nome(self):
        '''Retorna o nome da cidade.
        '''
        return 'Grumelinda do Sul'
    
    def qtd_cidadaos(self):
        '''Retorna a quantidade de cidadãos cadastrados na prefeitura.
        '''
        return 28
    
    def renda_media(self):
        '''Calcula a renda média dos cidadãos.
        '''
        return 1500.55

    def orcamento_renda_minima(self, renda_minima):
        '''Calcula o orçamento necessário para garantir que todo cidadão
        receba pelo menos uma renda mínima.
        Retorna uma tupla contendo o orçamento calculado e a quantidade
        de cidadãos beneficiado.
        '''
        return (40000, 22)
    
    
    def renda_media_de_faixa_etaria(self, idade_inf, idade_sup, ano_atual):
        '''Calcula a renda média dos cidadãos que estão dentro de uma faixa
        etária.
        Retorna a renda média calculada ou então None para indicar que não
        há nenhum cidadão dentro da faixa etária.
        '''
        return 3450.24
    
    def qtd_idosos(self, idade_idoso, ano_atual):
        '''Calcula a quantidade de cidadãos idosos existente em determinado ano. 
        É considerado idoso qualquer cidadão cuja idade seja maior ou igual à idade informada.
        '''
        return 7
    
    def cidadaos_com_mais_renda_que(self, renda):
        '''Retorna uma lista de cidadãos cuja renda seja superior à renda informada.
        '''
        return []
    
    def n_cidadaos_com_menos_renda_que(self, n, renda):
        '''Retorna uma lista com os N primeiros cidadãos cadastrados cuja renda seja
        inferior à renda informada.
        Obs: Nem sempre haverá N cidadãos nesta situação.
        '''
        return []


