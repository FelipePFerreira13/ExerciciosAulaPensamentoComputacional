def testeFilme():
    
    from models.Filme import Filmes
    
    teste = Filmes("John Wick", "Ação", 101, 8.5)
    
    teste.avaliar(11)
    teste.avaliar(9)
    
    teste.exibir_informacoes()
    