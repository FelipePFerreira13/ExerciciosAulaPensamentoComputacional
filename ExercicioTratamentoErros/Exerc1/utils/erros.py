class MinhaExcecao(Exception):
    pass

    def ValorNegativo(valor):
        if valor < 0:
            raise MinhaExcecao("Insira um valor positivo")
        else:
            ...