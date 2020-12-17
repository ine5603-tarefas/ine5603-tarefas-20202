# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Tribo
# --------------------------
# Classe que representa uma tribo de guerreiros.
#

from model.guerreiro import Guerreiro

class Tribo:
    def __init__(self, nome, qtd_max_guerreiros, qtd_max_vidas):
        '''Cria uma tribo sabendo-se o seu nome, a quantidade máxima
        de guerreiros que a tribo pode ter e o número máximo de vidas
        dos guerreiros da tribo.
        '''
        self._nome = nome
        self._QTD_MAX_GUERREIROS = qtd_max_guerreiros
        self._MAX_VIDAS = qtd_max_vidas
        self._guerreiros = {}  # armazenará guerreiros indexados pelo seu nome
        self._qtd_vivos = 0
        self._qtd_mortos = 0
        
        
    def nome(self):
        '''Retorna o nome da tribo.
        '''
        return self._nome
    
    def max_vidas(self):
        '''Retorna o número máximo de vidas de um guerreiro da tribo.
        '''
        return self._MAX_VIDAS
    
    def max_guerreiros(self):
        '''Retorna a quantidade máxima de guerreiros da tribo.
        '''
        return self._QTD_MAX_GUERREIROS
    
    def qtd_vivos(self):
        '''Retorna quantos guerreiros estão vivos.
        '''
        return self._qtd_vivos
    
    def qtd_mortos(self):
        '''Retorna quantos guerreiros estão mortos.
        '''
        return self._qtd_mortos
    
    def qtd_guerreiros(self):
        '''Retorna a quantidade total de guerreiros (vivos e mortos).
        '''
        return self._qtd_mortos + self._qtd_vivos
    
    def adicione_guerreiro(self, nome):
        '''Adiciona um guerreiro na tribo informando o nome do guerreiro.
        Retorna 0 para indicar que adicionou, 1 para indicar que a tribo
        está cheia e 2 para indicar que já existe um guerreiro com o nome
        informado.
        '''
        OK = 0
        SEM_LUGAR = 1
        JA_EXISTE = 2
        
        if self.qtd_guerreiros() == self._QTD_MAX_GUERREIROS:
            resposta = SEM_LUGAR
        elif self._guerreiros.get(nome) is not None:
            resposta = JA_EXISTE
        else:
            novoGuerreiro = Guerreiro(nome, self._MAX_VIDAS)
            self._guerreiros.update({nome:novoGuerreiro})
            self._qtd_vivos = self._qtd_vivos + 1
            resposta = OK
        return resposta
    
    def remova_guerreiro(self, nome):
        '''Remove um guerreiro a partir do seu nome.
        Retorna True se removeu ou False se não removeu porque
        não existe guerreiro com o nome informado.
        '''
        g = self._guerreiros.get(nome)
        if g is None:
            removeu = False
        else:
            removeu = True
            if g.esta_vivo():
                self._qtd_vivos -= 1
            else:
                self._qtd_mortos -= 1
            del self._guerreiros[nome]

        return removeu
    
    def cure(self, nome):
        '''Cura um guerreiro, ou seja, dá uma vida ao guerreiro.
        Retorna True para indicar que curou ou False para indicar
        que não há guerreiro com o nome informado.
        '''
        g = self._guerreiros.get(nome)
        if g is None:
            curou = False
        else:
            if not g.esta_vivo():
                self._qtd_vivos += 1
                self._qtd_mortos -= 1
            g.ganhe_vida()
            curou = True
        return curou
         
    def fira(self, nome):
        '''Fere um guerreiro, ou seja, tira uma vida do guerreiro.
        Retorna True para indicar que feriu ou False para indicar
        que não há guerreiro com o nome informado.
        '''
        g = self._guerreiros.get(nome)
        if g is None:
            feriu = False
        else:
            feriu = True
            estava_vivo = g.esta_vivo()
            g.perca_vida()
            if estava_vivo and not g.esta_vivo():
                self._qtd_vivos -= 1
                self._qtd_mortos += 1
        return feriu
    
    def guerreiro(self, nome):
        '''Retorna uma cópia do guerreiro com o nome informado ou None
        para indicar que não há guerreiro com aquele nome.
        '''
        g = self._guerreiros.get(nome)
        if g is not None:
            g = g.copia()
        return g
    
    def vivos(self):
        '''Retorna um dicionário contendo cópias dos guerreiros vivos, indexados
        pelos nomes dos guerreiros.
        '''
        vivos = {}
        for g in self._guerreiros.values():
            if g.esta_vivo():
                vivos.update({g.nome() : g.copia()})
        return vivos
    
    def mortos(self):
        '''Retorna um dicionário contendo cópias dos guerreiros mortos, indexados
        pelos nomes dos guerreiros.
        '''
        mortos = {}
        for g in self._guerreiros.values():
            if not g.esta_vivo():
                mortos.update({g.nome():g.copia()})
        return mortos
