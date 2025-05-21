from models.Veiculo import Veiculo
from models.Carro import Carro
from models.Caminhao import Caminhao
from models.Moto import Moto
from models.Frota import Frota


carro1 = Carro("aaa1a11", "Carro", "Teste", 2025, "Prata", 2000, "Gasolina", 4, 5, 300, "teste", 50)
moto1 = Moto("bbb2b22", "Moto", "Teste", 2025, "Prata", 2000, "Gasolina", 200, "teste", 50)
caminhao1 = Caminhao("ccc3c33", "Caminhao", "Teste", 2025, "Prata", 2000, "Gasolina", 2, 3, 500, "teste", 50)
frota1 = Frota()


frota1.adicionar_veiculo(carro1)
frota1.adicionar_veiculo(moto1)
frota1.adicionar_veiculo(caminhao1)

for veiculo in frota1.__str__():
    print(veiculo)
    
print(f"O consumo total da frota foi {frota1.consumo_total(100)} litros")