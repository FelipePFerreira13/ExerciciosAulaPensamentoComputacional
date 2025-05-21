import re
from models.Veiculo import Veiculo
from models.Carro import Carro
from models.Carro_Eletrico import Carro_Eletrico
from models.Moto import Moto

placa = "AAA1A11"
carro1 = Carro(placa, "Carro", "Teste", 2025, "Prata", 2000, "Gasolina", 4, 5, 300, "teste", 50)

placa = "BBB2B22"
moto1 = Moto(placa, "Moto", "Teste", 2025, "Prata", 2000, "Gasolina", 200, "teste", 50)

placa = "CCC2333"
carro_eletrico1 = Carro_Eletrico(placa, "Carro Eletrico", "Teste", 2025, "Prata", 2000, "Litio", 2, 3, 50)
    
print(f"O consumo do carro foi {carro1.calcular_consumo(150)} L")
print(f"O consumo da moto foi {moto1.calcular_consumo(150)} L")
print(f"O consumo do carro eletrico foi {carro_eletrico1.calcular_consumo(150)} kWh")

while True:
    placa = input("Insira uma nova placa para o carro: ")
    if placa == 's' or placa == 'S':
        print("Você está saindo")
        break
    elif carro1.set_placa(placa):
        print("Nova placa aceita")
    else:
        print("Nova placa rejeitada")
    placa = input("Insira uma nova placa para a moto: ")
    if placa == 's' or placa == 'S':
        print("Você está saindo")
        break
    elif moto1.set_placa(placa):
        print("Nova placa aceita")
    else:
        print("Nova placa rejeitada")
    placa = input("Insira uma nova placa para o carro eletrico: ")
    if placa == 's' or placa == 'S':
        print("Você está saindo")
        break
    elif carro_eletrico1.set_placa(placa):
        print("Nova placa aceita")
    else:
        print("Nova placa rejeitada")
    print(carro1)
    print(moto1)
    print(carro_eletrico1)