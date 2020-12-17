# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício do Navio
# --------------------------
# Classe que representa um container.
#

class Container:
    '''Um container é caracterizado pelo seu código de identificação,
    se é refrigerado ou não e pelo peso das mercadorias que ele armazena.
    '''
    def __init__(self, codigo, refrigerado, peso_mercadoria):
        peso_refrigeracao = 80 if refrigerado else 0
        self._CODIGO = codigo
        self._REFRIGERADO = refrigerado
        self._PESO_MERCADORIA = peso_mercadoria
        self._PESO = peso_mercadoria + peso_refrigeracao
        
    def codigo(self):
        '''Retorna o código do container.
        '''
        return self._CODIGO

    def refrigerado(self):
        '''Retorna se o container é refrigerado (True) ou não (False).
        '''
        return self._REFRIGERADO
    
    def peso_mercadoria(self):
        '''Retorna o peso da mercadoria.
        '''
        return self._PESO_MERCADORIA

    def peso(self):
        '''Retorna o peso do container (peso da mercadoria + peso da refrigeração)
        '''
        return self._PESO
    
    def __str__(self):
        '''Retorna uma string representando os dados container.
        '''
        texto = 'codigo: {} refrigerado: {} peso_mercadoria: {} peso: {}'
        return texto.format(self._CODIGO, self._REFRIGERADO, self._PESO_MERCADORIA, self.peso())
