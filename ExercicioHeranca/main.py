from models.Veiculo import Veiculo
from models.CarroCombustao import Carro_Combustao
from models.CarroEletricos import Carro_Eletricos
from models.CarroConvEletrico import Carro_Conv_Eletrico




fusca_eletrico = Carro_Conv_Eletrico("AAA1A11", "Fusca", "Wolkswagen", 2020, "Azul", 80000, 4, 4, 50, 100, "Manual", 100, "Litio", "Autonomo")

print(fusca_eletrico)