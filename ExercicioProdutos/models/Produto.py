class Produto:
    
    
    def __init__(self, nome : str, preco : float, moeda : str = "BRL") -> None:
        self.__nome = nome
        self.__preco = preco 
        self.__moeda = moeda
        
    def __str__(self):
        infos = f"Nome: {self.__nome}"
        infos += f"\nPreço: {self.__preco}"
        infos += f"\nMoeda: {self.__moeda}"
        return infos
           
    def get_nome(self):
        return self.__nome
    def set_nome(self, valor : str):
        self.__nome = valor
    def get_preco(self):
        return self.__preco
    def set_preco(self, valor : float):
        self.__preco = valor
    def get_moeda(self):
        return self.__moeda
    def set_moeda(self, valor : str):
        self.__moeda = valor
    