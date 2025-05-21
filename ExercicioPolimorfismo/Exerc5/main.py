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
    
print(moto1 == carro1)
print(moto1 == carro_eletrico1)
print(carro_eletrico1 == carro1)