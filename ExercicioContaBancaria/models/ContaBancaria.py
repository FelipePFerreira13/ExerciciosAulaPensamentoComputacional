import time
class ContaBancaria:
    def __init__(self, titular : str, saldo : float = 0, limite : float = 500, historico: list = []) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = historico 
        print(f"Seu {self.titular} foi cadastrado com sucesso")

    
    def padrao_brasileiro(self, valor):
        return f"R${str(round(valor,2)).replace('.',',')}"
    
    def adiciona_historico(self, tipo_transferencia, valor, tempo, saldo, destinatario = None):
        
        if tipo_transferencia == "Saque":
            if destinatario == None:
                self.historico.append({"tipo": f"{tipo_transferencia}",
                                        "remetente": self.titular,
                                        "destinatario": destinatario,
                                        "valor": valor,
                                        "tempo": tempo,
                                        "saldo": saldo})
            else:
                self.historico.append({"tipo": f"Transferência - {tipo_transferencia}",
                                        "remetente": self.titular,
                                        "destinatario": destinatario.titular,
                                        "valor": valor,
                                        "tempo": tempo,
                                        "saldo": saldo})
        elif tipo_transferencia == "Deposito":
            if destinatario == None:
                self.historico.append({"tipo": f"{tipo_transferencia}",
                                        "remetente": destinatario,
                                        "destinatario": self.titular,
                                        "valor": valor,
                                        "tempo": tempo,
                                        "saldo": saldo})
            else:
                self.historico.append({"tipo": f"Transferência - {tipo_transferencia}",
                                        "remetente": destinatario.titular,
                                        "destinatario": self.titular,
                                        "valor": valor,
                                        "tempo": tempo,
                                        "saldo": saldo})
        else:
            print(f"Transação {tipo_transferencia} invalida")       

    def depositar(self, valor, destino = None):
        if valor > 0:
            self.__saldo += valor
            self.adiciona_historico("Deposito", valor, int(time.time()), self.saldo, destino)
            return True
        else:
            print("Insira um valor maior que zero para o deposito")
            return False            
        return True

    def sacar(self, valor, destino = None):
        if valor > 0 and valor <= self.saldo:
            self.__saldo -= valor
            self.adiciona_historico("Saque", valor, int(time.time()), self.saldo, destino)
            
            print(f"O saque de valor {self.padrao_brasileiro(valor)} foi concluido")
        elif valor <= self.saldo + self.limite and self.saldo - valor >= -self.limite:
            usar_limite = input(f"Gostaria de usar seu limite, R${self.padrao_brasileiro(self.limite)}, para a operação? (S/N)")
            if usar_limite == 's' or usar_limite == 'S':
                self.__saldo -= valor
                self.adiciona_historico("Saque", valor, int(time.time()), self.saldo, destino)
                return True
            else:
                print("Não será usado o limite, saldo insuficiente")
                return False
        else:
            print("Insira um valor maior que zero para o saque e menor que o seu limite")
            return False
       
        return True

    def transferir(self, destinatario, valor):
        self.sacar(valor, destinatario)
        destinatario.depositar(valor, self)
        
    def exibir_historico(self):
        print("Histórico: \n")
        for transacao in self.historico:
            dt = time.localtime(transacao["tempo"])
            msg =  f"Tipo: {transacao["tipo"]}\n"
            msg += f"Remetente: {transacao["remetente"]}\n"
            msg += f"Destinatario: {transacao["destinatario"]}\n"
            msg += f"Valor: {transacao["valor"]}\n"
            msg += f"Saldo: {transacao["saldo"]}\n"
            msg += f"Data: {dt.tm_mday}:{dt.tm_mon}:{dt.tm_year}\n"
            msg += f"Tempo: {dt.tm_hour}:{dt.tm_min}:{dt.tm_sec}\n"
            print(msg)
        
    @property    
    def saldo(self):
        return self.__saldo 
    @property    
    def titular(self):
        return self.__titular
    @property    
    def limite(self):
        return self.__limite 
    @property    
    def historico(self):
        return self.__historico 
        
    # @saldo.setter
    # def saldo(self, saldo):
    #     self.__saldo = saldo
    # @titular.setter    
    # def titular(self, titular):
    #     self.__titular = titular
    # @limite.setter    
    # def limite(self, limite):
    #     self.__limite = limite
    # @historico.setter    
    # def historico(self, historico):
    #     self.__historico = historico
    
        