from models.Veiculo import Veiculo
from models.Carro import Carro
from models.Caminhao import Caminhao
from models.Moto import Moto


Carro1 = Carro("aaa1a11", "Carro", "Teste", 2025, "Prata", 2000, "Gasolina", 4, 5, 300, "teste", 50)
Moto1 = Moto("bbb2b22", "Moto", "Teste", 2025, "Prata", 2000, "Gasolina", 200, "teste", 50)
caminhao1 = Caminhao("ccc3c33", "Caminhao", "Teste", 2025, "Prata", 2000, "Gasolina", 2, 3, 500, "teste", 50)

while True:
    distancia = input("Qual a distancia que quer verificar? Digite 's' para sair \n")
    if distancia == 's' or distancia == 'S':
        break
    distancia = float(distancia)
    print(f"O carro consume consume {Carro1.calcular_consumo(distancia)} litros na viagem")
    print(f"A moto consume {Moto1.calcular_consumo(distancia)} litros na viagem")
    print(f"O caminhão consume {caminhao1.calcular_consumo(distancia)} litros na viagem")