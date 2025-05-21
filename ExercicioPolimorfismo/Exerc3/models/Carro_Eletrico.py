from .Veiculo import Veiculo

class Carro_Eletrico(Veiculo):
    
    def __init__(self,
                 placa: str,
                 modelo: str,
                 marca: str,
                 ano: int,
                 cor: str,
                 valor_fipe: float,
                 tipo_bateria : str,
                 nPortas: int,
                 nAssentos: int,
                 nivel_bateria: int) -> None:
        Veiculo.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        self.__tipo_bateria = tipo_bateria
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nivel_bateria = nivel_bateria
    
    def __str__(self) -> str:
        """
        Retorna uma string com as informações do carro de combustão
        """
        # Reutiliza o método __str__ da classe pai (Veiculos)
        infos = super().__str__()
        # Adiciona as informações especificas do carro eletrico
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Número de assentos: {self.__nAssentos}\n"
        return infos
    
    def calcular_consumo(self, distancia):
        return distancia/0.15