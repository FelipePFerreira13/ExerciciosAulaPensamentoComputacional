from .Veiculo import Veiculo

class Carro_Combustao(Veiculo):
    def __init__(self, placa : str, modelo : str, marca : str, ano : int, cor : str, valor_fipe : float,
                 n_portas : int, n_acentos : int, tamanho_tanque : float, nivel_combustivel: float, n_cambio : str) -> bool:
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__n_portas = n_portas
        self.__n_acentos = n_acentos
        self.__tamanho_tanque = tamanho_tanque
        self.__nivel_combustivel = nivel_combustivel
        self.__n_cambio = n_cambio
        
        
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"\nNúmero de portas: {self.__n_portas}"
        infos += f"\nNúmero de acentos: {self.__n_acentos}"
        infos += f"\nTamanho do tanque: {self.__tamanho_tanque}"
        infos += f"\nNível do tanque: {self.__nivel_combustivel}"
        infos += f"\nCambio: {self.__n_cambio}"
        
        return infos
        
    def abastever(self, percentual : float) -> bool:
        novo_percentual = self.__nivel_combustivel + percentual
        if novo_percentual <= 100:
            self.__nivel_combustivel = novo_percentual
            return True
