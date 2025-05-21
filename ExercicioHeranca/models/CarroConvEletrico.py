from .CarroCombustao import Carro_Combustao

class Carro_Conv_Eletrico(Carro_Combustao):
    def __init__(self, placa : str, modelo : str, marca : str, ano : int, cor : str, valor_fipe : float,
                 n_portas : int, n_acentos : int, tamanho_tanque : float, nivel_combustivel: float, n_cambio : str,
                 nivel_bateria : int, tipo_bateria : str, autonomia : str) -> bool:
        
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe, n_portas, n_acentos, tamanho_tanque , nivel_combustivel, n_cambio)

        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia

    def __str__(self):
        infos = super().__str__()
        infos += f"\nNivel bateria: {self.__nivel_bateria}"
        infos += f"\nTipo bateria: {self.__tipo_bateria}"
        infos += f"\nAutonomia: {self.__autonomia}"
        return infos
        