from utils.erros import MinhaExcecao
from models.Veiculo import Veiculo
from models.Carro import Carro
from models.Carro_Eletrico import Carro_Eletrico
from models.Moto import Moto

placa = "AAA1A11"
carro1 = Carro(placa, "Carro", "Teste", 2025, "Prata", 2000, "Gasolina", 4, 5, 300, "teste", 50)

placa = "AAA1A11"
moto1 = Moto(placa, "Moto", "Teste", 2025, "Prata", 2000, "Gasolina", 200, "teste", 50)

placa = "CCC2333"
carro_eletrico1 = Carro_Eletrico(placa, "Carro Eletrico", "Teste", 2025, "Prata", 2000, "Litio", 2, 3, 50)
    
while True:
    try:
        entrada = float(input("Insira a distancia para calcular consumo ou 's' para sair: "))
        if entrada = 's' or entrada = 'S':
            break
        MinhaExcecao.ValorNegativo(entrada)
        print( carro1.calcular_consumo(entrada))
        print( carro_eletrico1.calcular_consumo(entrada))
        print( moto1.calcular_consumo(entrada))
    except MinhaExcecao as erro:
        print(erro)