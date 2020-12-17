# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício do relógio
# --------------------------
# Classe que representa um relógio, que é um objeto que representa um
# instante no tempo (hora, minuto e segundo).

class Relogio:
    def __init__(self, hora=0, minuto=0, segundo=0):
        '''Cria um relógio que marca inicialmente uma hora, um minuto e um segundo.
        '''
        pass

    def mude_hora(self, hora):
        '''Altera a hora marcada pelo relógio.
        '''
        pass
        
    def mude_minuto(self, minuto):
        '''Altera o minuto marcado pelo relógio.
        '''
        pass
        
    def mude_segundo(self, segundo):
        '''Altera o segundo marcado pelo relógio.
        '''
        pass
        
    def hora(self):
        '''Retora a hora marcada pelo relógio.
        '''
        return 17
    
    def minuto(self):
        '''Retorna o minuto marcado pelo relógio.
        '''
        return 23
    
    def segundo(self):
        '''Retorna o segundo marcado pelo relógio.
        '''
        return 34
    
    def mude_hms(self, hora, minuto, segundo):
        '''Altera a hora, o minuto e o segundo marcados pelo relógio.
        '''
        pass

    def hms(self):
        '''Retorna uma tupla contendo a hora, o minuto e o segundo
        marcados pelo relógio.
        '''
        return (8, 37, 55)
    
    def tick(self):
        '''Faz com que o relógio seja atualizado em mais um segundo.
        Obs: atualiza os minutos e as horas caso necessário.
        '''
        pass

    def compare_com(self, outro_relogio):
        '''Compara o relógio com outro relógio. Há três resultados possíveis:
        a) ambos os relógios marcam o mesmo horário.
        b) o relógio está atrasado em relação ao outro relógio.
        c) o relógio está adiantado em relação ao outro relógio.
        Assim, como convenção, o método deve retornar:
        0  no caso a)
        -1 no caso b)
        +1 no caso c
        '''            
        return 0
        