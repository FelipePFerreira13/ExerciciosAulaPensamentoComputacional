# A partir do exemplo, complete com a classe 'Proprietario', onde terá:
# - Atributos: nome, cpf e placas de veículos que adquiriu;
# - métodos: criar proprietário, validar, adicionar/remover veículo
class Proprietario:
    
    def __init__(self, nome : str, cpf : str, placas : list = list()):

        self.__nome = nome
        self.__cpf = cpf    
        self.__placas = placas
        
    
    
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf 
    def get_placas(self):
        return self.__placas