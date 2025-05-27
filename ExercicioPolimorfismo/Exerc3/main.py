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

carro_eletrico1.recarregar() 

print(f"O consumo do carro foi {carro1.calcular_consumo(150)} L")
print(f"O consumo da moto foi {moto1.calcular_consumo(150)} L")
print(f"O consumo do carro eletrico foi {carro_eletrico1.calcular_consumo(150)} kWh")
