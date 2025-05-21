class Veiculo:
    def __init__(self, placa : str, modelo : str, marca : str, ano : int, cor : str, valor_fipe : float) -> None:
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano 
        self.__cor = cor 
        self.__valor_fipe = valor_fipe
        
    def __str__(self) -> str:
        return f"Placa: {self.__placa}\nModelo: {self.__modelo}\nMarca: {self.__marca}\nAno: {self.__ano}\nCor {self.__cor}\nValor Fipe: {self.__valor_fipe}"
        
        
    @property
    def placa(self):
        return self.__placa