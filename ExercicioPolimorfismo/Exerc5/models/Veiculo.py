import re

class Veiculo:
    """
    Classe com as principais funcionalidades do sistema de veiculos, como placas, veiculos, etc.
    """

    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        """Construtor da classe Veiculo"""
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe

    def __str__(self) -> str:
        """Retorna uma string com as informações do veiculo"""
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe}\n"
        return infos
    
    def __eq__(self, other):
        if isinstance(other, Veiculo):
            return self.__placa == other.__placa
        return False

    def set_placa(self,nova_placa) -> bool:
        """Retorna a placa do veiculo"""
        if re.match("[A-Z][A-Z][A-Z][0-9][A-Z][0-9][0-9]", nova_placa):    
            self.__placa = nova_placa
            return True
             
    def get_placa(self) -> str:
        """Retorna a placa do veiculo"""
        return self.__placa

    def setValorFipe(self, valor: float) -> None:
        """Método que altera o valor da Fipe do Veículo

        Argumento: valor (float): novo valor da Fipe
        Saída: True se ok
        """
        self.__valor_fipe = valor
        return True
