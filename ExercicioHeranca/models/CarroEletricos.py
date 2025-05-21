from .Veiculo import Veiculo

class Carro_Eletricos(Veiculo):
    def __init__(self, placa : str, modelo : str, marca : str, ano : int, cor : str, valor_fipe : float,
                 n_portas : int, n_acentos : int, nivel_bateria : int, tipo_bateria : str, autonomia : str) -> None:
        super().__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        self.__n_portas = n_portas
        self.__n_acentos = n_acentos
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
        
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"\nNúmero de portas: {self.__n_portas}"
        infos += f"\nNúmero de acentos: {self.__n_acentos}"
        infos += f"\nNivel bateria: {self.__nivel_bateria}"
        infos += f"\nTipo bateria: {self.__tipo_bateria}"
        infos += f"\nAutonomia: {self.__autonomia}"
        return infos