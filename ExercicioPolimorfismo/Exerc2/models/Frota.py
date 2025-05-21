class Frota:
    
    def __init__(self):
        self.__lista = list()
        self.__quantidade = 0
    
    def __str__(self) -> list:
        lista_print = []
        for veiculo in self.__lista:
            lista_print.append(veiculo.__str__())
        return lista_print
        
    def adicionar_veiculo(self, veiculo):
        self.__lista.append(veiculo)
        self.__quantidade += 1
        return True
    
    def consumo_total(self, distancia : float) -> float:
        consumo = 0
        for veiculo in self.__lista:
            consumo += veiculo.calcular_consumo(distancia)
        return consumo
