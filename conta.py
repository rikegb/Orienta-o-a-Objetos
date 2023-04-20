class Conta : 

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto . . . {}" .format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo de R$ {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel =self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor R${} passou do limite".format(valor))
        
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)
       
    @property
    def get_saldo(self):
        return self.__saldo
        
    @property
    def get_titular(self):
        return self.__titular

    @property
    def get_limite(self):
        return self.__limite

    @property
    def set_limite(self,limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
