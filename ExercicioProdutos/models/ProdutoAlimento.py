from .Produto import Produto
class ProdutoAlimento(Produto):
    
    def __init__(self, nome : str, preco : float) -> None :
        Produto.__init__(self,nome=nome,preco=preco)
        
    def __str__(self):
        infos = Produto.__str__(self)
        infos += f"\nTipo: Alimento"
        return infos
           