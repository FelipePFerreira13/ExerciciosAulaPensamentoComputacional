from models.ContaBancaria import ContaBancaria

def testeContaBancaria():
    print("Teste banco")

    contas = list()
    for i in range(10):
        nome = f"teste{i}"

        contas.append(ContaBancaria(nome))
        di = {nome : i}
        