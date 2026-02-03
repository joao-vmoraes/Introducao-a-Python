from abc import ABC, abstractmethod

class FalhaNaAutenticacaoError(Exception): ...

class Conta(ABC):
    def __init__(self, agencia: str, numero:int, saldo: float = 0):
        self._agencia:str = agencia
        self._numero:int = numero
        self._saldo:float = saldo
    
    def __repr__(self):
        return f'AGENCIA: {self.agencia} , NUMERO: {self.numero} , SALDO: {self.saldo}'

    @property 
    def agencia(self)->str: return self._agencia

    @property
    def numero(self)-> int: return self._numero

    @property
    def saldo(self) -> float: return self._saldo

    @agencia.setter
    def agencia(self, valor: str)->None:self._agencia = valor

    @numero.setter
    def numero(self, valor:int)->None: self._numero = valor

    @saldo.setter
    def saldo(self, valor:float)->None: self._saldo = valor

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:
        self.saldo += valor
        return True


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo)

    def sacar(self, valor):
        saque_sucedido = False
        if valor > self.saldo:
            print("Saldo insuficiente")
            return saque_sucedido
        else:
            self.saldo -= valor
            saque_sucedido = True
            print("Valor sacado com sucesso")
            return saque_sucedido


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    def __repr__(self):
        resultado = super().__repr__()
        return resultado + f' , LIMITE: {self.limite}'

    @property
    def limite(self): return self._limite

    @limite.setter
    def limite(self, valor): self._limite = valor

    def sacar(self, valor):
        saque_sucedido = False
        if valor > self.saldo + self.limite:
            print("Saldo e limite insuficiente.")
            return saque_sucedido
        elif valor < self.saldo:
            self.saldo -= valor
            print("Valor sacado com sucesso.")
            saque_sucedido = True
            return saque_sucedido
        else:
            valor_restante = valor - self.saldo
            self.saldo = 0
            self.limite -= valor_restante
            saque_sucedido = True
            print("Valor sacado com sucesso")
            return saque_sucedido


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


    def __repr__(self):
        return f' , NOME: {self.nome} , IDADE: {self.idade}'

    @property
    def nome(self): return self._nome

    @nome.setter
    def nome(self, valor): self._nome = valor
    
    @property
    def idade(self): return self._idade

    @idade.setter
    def idade(self, valor): self._idade = valor


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta: Conta):
        super().__init__(nome, idade)
        self._conta = conta

    def __repr__(self):
        return  self.conta.__repr__() + super().__repr__()

    @property
    def conta(self): return self._conta

    @conta.setter
    def conta(self, conta: Conta): self._conta = conta

class Banco:
    agencias = ['0001']

    def __init__(self, clientes:  list[Cliente] = [], contas:  list[Conta] = []):
        self.clientes = clientes
        self.contas = contas

    def adicionar_cliente(self, cliente:Cliente):
        self.clientes.append(cliente)
        self.contas.append(cliente.conta)

    def autenticar_saque(self, cliente:Cliente):
        autenticacao = (cliente in self.clientes and cliente.conta.agencia in self.agencias and cliente.conta in self.contas)
        return autenticacao

    def sacar(self, cliente: Cliente, valor : float):
        if self.autenticar_saque(cliente):
            return cliente.conta.sacar(valor)
        raise FalhaNaAutenticacaoError("Dados invalidos ou inexistentes.")



#====================================================

banco_minha_casa = Banco()

c1 = ContaPoupanca("0001" , 132, 100)
joao = Cliente("joao", 19, c1)

c2 = ContaCorrente("0001", 412, 200, 50)
eduarda = Cliente("Eduarda", 20, c2)

banco_minha_casa.adicionar_cliente(joao)
banco_minha_casa.adicionar_cliente(eduarda)

banco_minha_casa.sacar(joao, 101)
banco_minha_casa.sacar(eduarda, 240)

print(joao)
print(eduarda)