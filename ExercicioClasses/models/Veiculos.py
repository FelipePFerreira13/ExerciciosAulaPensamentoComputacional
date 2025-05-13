class Veiculos:
    def __init__(self, marca, modelo, ano, placa, cor, latitude = 0, longitude = 0, velocidade = 0):
        self._modelo = modelo
        self._marca = marca 
        self._ano = ano
        self._placa = placa
        self._cor = cor 
        self._latitude = latitude 
        self._longitude = longitude
        self._velocidade = velocidade
        print(f"Seu {self.modelo} foi cadastrado com sucesso")
        
    def ver_velocidade(self):
        print(f"O carro modelo {self.modelo}, placa {self.placa} está com uma velocidade de {self.velocidade}")
        
    def acelerar(self, aceleracao, tempo):
        if aceleracao < 0:
            # marcha seria a função
            print("Para dar ré, utilize a função Ré")
            return 
        self._velocidade += aceleracao * tempo
    
    def re(self, aceleracao, tempo):
        if aceleracao > 0:
            # marcha seria a função
            print("Para acelerar, utilize a função Acelerar")
            return 
        self._velocidade -= aceleracao * tempo
        
    def frear(self, freio, tempo):
        if self._velocidade > 0:
            self._velocidade -= freio * tempo
            if self._velocidade < 0:
                self._velocidade = 0 
        elif self._velocidade < 0:
            self._velocidade += freio* tempo
            if self._velocidade > 0:
                self._velocidade = 0 
        
        
    @property    
    def marca(self):
        return self._marca 
    @property    
    def modelo(self):
        return self._modelo 
    @property    
    def ano(self):
        return self._ano 
    @property    
    def placa(self):
        return self._placa 
    @property    
    def cor(self):
        return self._cor 
    @property    
    def latitude(self):
        return self._latitude 
    @property    
    def longitude(self):
        return self._longitude 
    @property    
    def velocidade(self):
        return self._velocidade 
        
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    @modelo.setter    
    def modelo(self, modelo):
        self._modelo = modelo
    @ano.setter    
    def ano(self, ano):
        self._ano = ano
    @placa.setter    
    def placa(self, placa):
        self._placa = placa
    @cor.setter    
    def cor(self, cor):
        self._cor = cor
    @latitude.setter    
    def latitude(self, latitude):
        self._latitude = latitude
    @longitude.setter    
    def longitude(self, longitude):
        self._longitude = longitude
    @velocidade.setter    
    def velocidade(self, velocidade):
        self._velocidade = velocidade
        
        
    
        