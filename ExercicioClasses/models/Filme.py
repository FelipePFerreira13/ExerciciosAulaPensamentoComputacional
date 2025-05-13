class Filmes:
    
    def __init__(self, titulo, genero, duracao, avaliacao = 0):
        self._titulo = titulo
        self._genero = genero 
        self._duracao = duracao
        self._avaliacao = avaliacao
        print(f"Filme {self.titulo} foi cadastrado com sucesso")

    def avaliar(self, nova_nota):
        if nova_nota <= 10 and nova_nota >=0:
            self.avaliacao = nova_nota
            print("Nota alterada")
        else:
            print("As notas notas validas são de 0 a 10")
            
    def exibir_informacoes(self):
        msg = f"O filme {self.titulo}, do genero {self.genero}, "
        msg += f"tem duracao de {self.duracao} minutos e uma nota de {self.avaliacao}"
        print(msg)


    @property    
    def titulo(self):
        return self._titulo 
    @property    
    def genero(self):
        return self._genero 
    @property    
    def duracao(self):
        return self._duracao 
    @property    
    def avaliacao(self):
        return self._avaliacao 
        
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    @genero.setter    
    def genero(self, genero):
        self._genero = genero
    @duracao.setter    
    def duracao(self, duracao):
        self._duracao = duracao
    @avaliacao.setter    
    def avaliacao(self, avaliacao):
        self._avaliacao = avaliacao
