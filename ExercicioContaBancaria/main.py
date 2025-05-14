import os
import time
from models.ContaBancaria import ContaBancaria 


msg = "Selecione qual função quer utilizar:\n"
msg += "1 - Criar conta\n"
msg += "2 - Exibir Saldo\n"
msg += "3 - Sacar\n"
msg += "4 - Depositar\n"
msg += "5 - Realizar Transferência\n"
msg += "6 - Exibir histórico de transações\n"
msg += "7 - Excluir uma conta\n"
msg += "0 - Sair do sistema\n"

contas_banco = list()
titulares = list()

contas_banco.append(ContaBancaria("Banco"))

os.system('cls' if os.name == 'nt' else 'clear')

nome = input(f"Insira o nome do 1° titular: ")
contas_banco.append(ContaBancaria(nome))

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    if len(contas_banco) == 1:
        nome = input(f"Nenhuma conta detectada\nInsira o nome do 1° titular: ")
        contas_banco.append(ContaBancaria(nome))

        os.system('cls' if os.name == 'nt' else 'clear')


    funcao = int(input(msg))
    if funcao == 0:
        sair = input("Tem certeza que deseja sair? (s/n) \nTodos os dados serão perdidos")
        if sair == 's': 
            break
        elif sair == 'n':
            print("Saída do sistema cancelada")
        else:
            print("Comando desconhecido, cancelando operação")
    elif funcao == 1:
        nome = input(f"Insira o nome do {len(contas_banco)}° titular: ")
        if nome not in titulares:
            contas_banco.append(ContaBancaria(nome))
            titulares.append(nome)
        else:
            print("Titular já possui conta no banco")

    elif funcao == 2:
        nome = input("Insira o nome da conta que quer verificar: ")
        for conta in contas_banco:
            if conta.titular == nome:
                print(f"O saldo da conta com titular {nome} é R${conta.saldo}")   
                break     
        else:
            print("Nenhum titular com esse nome")
    elif funcao == 3:
        nome = input("Insira o nome da conta que quer sacar: ")
        for conta in contas_banco:
            if conta.titular == nome:
                if conta.saldo > conta.limite*-1:
                    valor = float(input(f"O quanto quer sacar? Seu saldo atual é R${conta.saldo}, com limite de R${conta.limite} "))
                    conta.sacar(valor)   
                break     
        else:
            print("Nenhum titular com esse nome")
    elif funcao == 4:
        nome = input("Insira o nome da conta que quer depositar: ")
        for conta in contas_banco:
            if conta.titular == nome:
                if conta.saldo > conta.limite*-1:
                    valor = float(input(f"O quanto quer depositar? "))
                    conta.depositar(valor)   
                break     
        else:
            print("Nenhum titular com esse nome")
    elif funcao == 5:
        nome = input("Insira o nome da conta remetente: ")
        for conta in contas_banco:
            if conta.titular == nome:
                transfere = input("Insira a conta destinatário: ")   
                for conta2 in contas_banco:
                    if transfere == conta2.titular:
                        valor = float(input("Insira o quanto quer transferir: "))
                        conta.transferir(conta2, valor)    
                        break
    elif funcao == 6:
        nome = input("Insira o nome da conta que quer sacar: ")
        for conta in contas_banco:
            if conta.titular == nome:
                conta.exibir_historico()
                break
        else:
            print("Conta não encontrada")
            
    elif funcao == 7:
        nome = input("Insira o nome da conta que quer deletar: ")
        for conta in contas_banco:
            if conta.titular == nome:
                if conta.saldo != 0:
                    if conta.saldo > 0:
                        transfere = input(f"Você possui R${conta.saldo} na conta, para qual conta precisamos transferir o dinheiro? ")
                        for conta2 in contas_banco:
                            if conta2.titular == transfere:                                    
                                conta.transferir(conta2, conta.saldo)
                                break
                        else:
                            transfere = input(f"Nenhuma conta com o titular detectado, gostaria de transferir para a conta do banco (s/n)? ")
                            if transfere == "s":
                                conta.transferir(contas_banco(0), conta.saldo)
                            else:
                                print("Conta com valor de saldo diferente de 0, exclusão cancelada")
                    
                    else:
                        transfere = input(f"Você está devendo R${conta.saldo} na conta, de quer transferir o dinheiro (s/n)? ")
                        if transfere == 's':
                            conta.depositar(abs(conta.saldo))
                        elif transfere == 'n':
                            
                            print("Exclusão cancelada")
                else:
                    contas_banco.remove(conta)
                    break     
            
        else:
            print("Nenhum titular com esse nome")
    
    input("\nClique 'Enter' para prosseguir ")    
    os.system('cls' if os.name == 'nt' else 'clear')
