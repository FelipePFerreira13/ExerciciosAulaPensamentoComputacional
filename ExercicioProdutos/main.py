from models.Produto import Produto
from models.ProdutoAlimento import ProdutoAlimento
from models.ProdutoEletronico import ProdutoEletronico
from utils.ConversorMoeda import ConversorMoeda


produto_base = Produto("Produto teste",100)
produto_alimento = ProdutoAlimento("Alimento teste",100)
produto_eletronico = ProdutoEletronico("Eletronico teste",100)


if ConversorMoeda.conversor_preco_para_brl(produto_base):
    print(f"{produto_base}\n")
else:
    print("O item já tem moeda BRL\n")
if ConversorMoeda.conversor_preco_para_eur(produto_eletronico):
    print(f"{produto_eletronico}\n")
else:
    print("O item já tem moeda EUR\n")
if ConversorMoeda.conversor_preco_para_usd(produto_alimento):
    print(f"{produto_alimento}\n")
else:
    print("O item já tem moeda USD\n")
