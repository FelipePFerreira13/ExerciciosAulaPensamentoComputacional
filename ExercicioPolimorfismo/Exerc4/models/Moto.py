from .Veiculo import Veiculo

class Moto(Veiculo):
    
    def __init__(self,
                 placa: str,
                 modelo: str,
                 marca: str,
                 ano: int,
                 cor: str,
                 valor_fipe: float,
                 tipo_combustivel : str,
                 nCilindrada: int,
                 nCambio: str,
                 nivel_combustivel: int) -> None:
        Veiculo.__init__(self, 
                         placa=placa, 
                         modelo=modelo, 
                         marca=marca, 
                         ano=ano, 
                         cor=cor, 
                         valor_fipe=valor_fipe)
        self.__tipo_combustivel = tipo_combustivel
        self.__nCilindrada = nCilindrada
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel
    
    def __str__(self) -> str:
        """
        Retorna uma string com as informações do carro de combustão
        """
        # Reutiliza o método __str__ da classe pai (Veiculos)
        infos = super().__str__()
        # Adiciona as informações especificas do carro a combustão
        infos += f"Combustivel: {self.__tipo_combustivel}\n"
        infos += f"Número de cilindrada: {self.__nCilindrada}\n"
        infos += f"Câmbio: {self.__nCambio}\n"
        infos += f"Nível Combustível: {self.__nivel_combustivel}\n"
        return infos
        
    def calcular_consumo(self, distancia):
        return distancia/20