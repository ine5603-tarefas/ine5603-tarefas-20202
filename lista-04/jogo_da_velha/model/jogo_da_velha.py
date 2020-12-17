
from model.tabuleiro import Tabuleiro

class JogoDaVelha:
    def __init__(self, humano, maquina, inicia):
        '''Um jogo é caracterizado por um jogador humano,
        um jogador máquina e a indicação de quem iniciará a partida.
        '''
        self._tabuleiro = Tabuleiro()
        self._humano = humano
        self._maquina = maquina
        self._inicia = inicia  # quem começa jogando: humano ou maquina
        self._proximo = inicia # próximo que joga
        
    def registre_jogada_humana(self, linha, coluna):
        '''Registra no tabuleiro a jogada definida pelo humano.
        Retorna True se a jogada foi válida (a casa estava vazia) ou False caso contrário.
        '''
        if self._inicia == 'humano':
            jogou = self._tabuleiro.marque_com_x(linha, coluna)
        else:
            jogou = self._tabuleiro.marque_com_o(linha, coluna)
        if jogou:
            self._proximo = 'maquina'
        return jogou

    def faca_maquina_jogar(self):
        '''Faz com que o jogador máquina marque sua jogada no tabuleiro.
        '''
        self._maquina.faca_jogada(self._inicia == 'maquina', self._tabuleiro)
        self._proximo = 'humano'

    def humano_deve_jogar(self):
        '''Retorna True se está na vez do jogador humano jogar.
        '''
        return self._proximo == 'humano'

    def nome_do_humano(self):
        '''Retorna o nome do jogador humano.
        '''
        return self._humano.nome()

    def nome_da_maquina(self):
        '''Retorna o nome do jogador máquina.
        '''
        return self._maquina.nome()

    def marca_do_humano(self):
        '''Retorna a marca (X ou O) que o humano deve usar.
        '''
        if self._inicia == 'humano':
            marca = self._tabuleiro.marca_x()
        else:
            marca = self._tabuleiro.marca_o()
        return marca

    def marca_da_maquina(self):
        '''Retorna a marca (X ou O) que a máquina deve usar.
        '''
        if self._inicia == 'maquina':
            marca = self._tabuleiro.marca_x()
        else:
            marca = self._tabuleiro.marca_o()
        return marca

    def terminou(self):
        '''Retorna True se a partida terminou (há algum vencedor ou não há mais casas vazias) ou False caso 
        contrário.
        '''
        return not self._tabuleiro.ha_casa_vazia() or self._tabuleiro.marca_do_vencedor() is not None

    def tabuleiro(self):
        '''Retorna o tabuleiro do jogo.
        '''
        return self._tabuleiro

    def vencedor(self):
        '''Retorna o jogador que venceu a partida ou None quando 
        não houver vencedor.
        '''
        marca_do_vencedor = self._tabuleiro.marca_do_vencedor()
        if marca_do_vencedor is None:
            vencedor = None
        else:
            if marca_do_vencedor == self._tabuleiro.marca_x():
                if self._inicia == 'humano':
                    vencedor = self._humano
                else:
                    vencedor = self._maquina
            else:
                if self._inicia == 'humano':
                    vencedor = self._maquina
                else:
                    vencedor = self._humano
        return vencedor
