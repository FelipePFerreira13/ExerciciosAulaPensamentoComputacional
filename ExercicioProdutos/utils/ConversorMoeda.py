from .erros import MoedaInvalidaError
class ConversorMoeda:
    
    def conversor_preco_para_usd(produto):
        if produto.get_moeda() == "USD":
            return False
        elif produto.get_moeda() == "EUR":
            produto.set_preco(produto.get_preco()*1.22)
            produto.set_moeda("USD")
            return True
        elif produto.get_moeda() == "BRL":
            produto.set_preco(produto.get_preco()/5.05)
            produto.set_moeda("USD")
            return True            
        else:
            raise MoedaInvalidaError("Moeda Invalida")

    def conversor_preco_para_eur(produto):
        if produto.get_moeda() == "EUR":
            return False
        elif produto.get_moeda() == "USD":
            produto.set_preco(produto.get_preco()/1.22)
            produto.set_moeda("EUR")
            return True
        elif produto.get_moeda() == "BRL":
            produto.set_preco(produto.get_preco()/5.05/1.22)
            produto.set_moeda("EUR")
            return True
        else:
            raise MoedaInvalidaError("Moeda Invalida")
            
    def conversor_preco_para_brl(produto):
        if produto.get_moeda() == "BRL":
            return False
        elif produto.get_moeda() == "USD":
            produto.set_preco(produto.get_preco()*5.05)
            produto.set_moeda("BRL")
            return True
        elif produto.get_moeda() == "EUR":
            produto.set_preco(produto.get_preco()*1.22*5.05)
            produto.set_moeda("BRL")
            return True
        else:
            raise MoedaInvalidaError("Moeda Invalida")
        
    