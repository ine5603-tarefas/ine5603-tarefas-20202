# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício da Prefeitura
# --------------------------
# Classe responsável por representar um cidadão.

class Cidadao:
    def __init__(self, ano_nascimento, renda):
        '''Um cidadão é caracterizado pelo seu ano de nascimento e sua renda.
        '''
        pass

    def ano_nascimento(self):
        '''Retorna o ano de nascimento do cidadão.
        '''
        return 1987
    
    def renda(self):
        '''Retorna a renda do cidadão.
        '''
        return 2000
    
    def idade(self, ano_atual):
        '''Retorna a idade do cidadão considerando um ano atual.
        '''
        return 26

    def __str__(self):
        '''Retorna string com os dados do cidadão.
        '''
        return 'Ano Nascimento: {} Renda: {}'.format(1977, 2300)
