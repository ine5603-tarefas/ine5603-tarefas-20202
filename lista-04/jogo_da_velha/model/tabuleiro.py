# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Jogo da Velha
# --------------------------
# Classe que representa um tabuleiro do jogo da velha.
#

class Tabuleiro:
    def __init__(self):
        '''Cria um tabuleiro e inicia todas as casas com vazio.
        '''
        self._marca_x = 'X'     # marca para jogadas X
        self._marca_o = 'O'     # marca para jogadas O
        self._marca_v = '.'     # marca indicando casa vazia
        l1 = [ self._marca_v ] * 3  # 3 casas vazias
        l2 = l1.copy()
        l3 = l1.copy()
        self._casas = [ l1, l2, l3 ]
        
    def marca(self, linha, coluna):
        '''Retorna a marca que está na casa linha e coluna.
        Atenção: linha e coluna podem ser 1, 2, ou 3.
        '''
        return self._casas[linha - 1][coluna - 1]
    
    def marque_com_x(self, linha, coluna):
        '''Tenta marcar com X a casa linha e coluna.
        Atenção: linha e coluna podem ser 1, 2 ou 3.
        Retorna True se conseguiu marcar ou False se não conseguiu 
        (porque a casa não estava vazia)
        '''
        return True
        
    def marque_com_o(self, linha, coluna):
        '''Tenta marcar com com O a casa linha e coluna.
        Atenção: linha e coluna podem ser 1, 2 ou 3.
        Retorna True se conseguiu marcar ou False se não conseguiu
        (poruqe a casa não estava vazia)
        '''
        return True
        
    
    def ha_casa_vazia(self):
        '''Retorna True se há pelo menos uma casa vazia ou False caso contrário.
        '''
        return True

    def marca_x_venceu(self):
        '''Retorna True se o jogador que marca com X venceu ou False caso contrário.
        '''
        return True
    
    def marca_o_venceu(self):
        '''Retorna True se o jogador que marca com O venceu ou False caso contrário.
        '''
        return True
    
            
    def marca_do_vencedor(self):
        '''Retorna a marca (X ou O) do vencedor ou None caso não haja vencedor.
        '''
        return self._marca_x
    
    def marca_x(self):
        '''Retorna o caracter usado pelo jogador que marca com X.
        '''
        return self._marca_x

    def marca_o(self):
        '''Retorna o caracer usado pelo jogador que marca com O.
        '''
        return self._marca_o

    def copia_casas(self):
        '''Retorna uma cópia (matriz 3 x 3) de todas as casas.
        '''
        l1 = self._casas[0].copy()
        l2 = self._casas[1].copy()
        l3 = self._casas[2].copy()
        return [l1, l2, l3]

