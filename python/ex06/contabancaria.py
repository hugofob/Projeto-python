'''from hashlib import sha256
from rich import print

class ContaBancaria:

    def __init__(self, _id, nome, saldo):
        chave =''

        self._id = _id # (#) protected
        self._nome = nome # (#) protected
        self._saldo = saldo # (#) protected
        self.__hash = sha256(chave.strip().encode('utf-8')).hexdigest() # (-) private

    def validar_senha(self, chave):
        usuario = sha256(chave.strip().encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print("[green]Senha confere[/]")
            return True
        else:
            print("[red]Senha incorreta![/]")
            return False

    def pede_senha(self):
        return input("Digite a senha: ")

    def saque(self, chave, valor):
        if not self.validar_senha(chave):
            return

        valor = abs(valor)

        if valor > self._saldo:
            print(f"[red]Saque NEGADO R$: {valor:,.2f} da conta {self._id}!!!SALDO INSUFICIENTE!!![/]")
        else:
            self._saldo -= valor
            print(f"[green]Saque de R$:{valor:,.2f} efetuado com sucesso conta {self._id}[/].")
            print(f"[blue]Saldo atual R$: {self._saldo:,.2f}[/]")

    def depositar(self, valor):
        valor = abs(valor)  # valor absoluto permanece o valor real
        self._saldo += valor
        print(f"[green]Depósito de R$:{valor:,.2f} autorizado na conta {self._id}[/].")
        print(f"[blue]Saldo atual R$: {self._saldo:,.2f}[/]")

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        novo_nome = novo_nome.strip()

        if len(novo_nome) == 0:
            raise ValueError("[red]Nome Vazio[/]")

        self._nome = novo_nome'''

from rich import print
from hashlib import sha256

class ContaBancaria:
    """
    Permita se criar uma conta bancaria onde irá fazer saques e depósitos
    """
    def __init__(self, id:int, nome:str=None, saldo:float=0, chave:str=None):
        self._id = id # protected (#)
        self._titular = nome # protected (#)
        self.__saldo = saldo # private (-)

        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f"[yellow]Conta {self._id} criada com sucesso, __saldo atual R$: {self.__saldo:,.2f}[/]")

    def pede_senha(self) ->str:
        from pwinput import pwinput # passoword asteriscos
        while True:
            senha = str(pwinput("Digite sua senha:")).strip()
            if len(senha) >= 6: # tamanho da sua senha
                break
        return senha

    def validar_senha(self, chave) ->bool: # confere se a senha e a mesma da chave fazendo um verdadeiro ou falso
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        #return f"A conta {self._id}, tem o _titular {self._titular} com __saldo R$:{self.__saldo:,.2f}"
        return f"Estado atual da conta -> {self.__dict__}."
    def deposito(self, valor):
        valor = abs(valor) # valor absoluto permanece o valor real
        self.__saldo += valor
        print(f"[green]Depósito de R$:{valor:,.2f} autorizado na conta {self._id}[/].")
        print(f"[blue]Saldo atual R$: {self.__saldo:,.2f}[/]")

    def saque(self, valor:float, chave:str=None):
        valor = abs(valor)

        if chave is None:# toda vez do saque se o usuario não informar a chave o método saque pede senha
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"[red]Saque NEGADO R$: {valor:,.2f} da conta {self._id}!!!SALDO INSUFICIENTE!!![/]")
            else:
                self.__saldo -= valor
                print(f"[green]Saque de R$:{valor:,.2f} efetuado com sucesso conta {self._id}[/].")
                print(f"[blue]Saldo atual R$: {self.__saldo:,.2f}[/]")
        else:
            print("Senha não confere, saque não autorizado!!!")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def nome(self):
        return self._titular
    @nome.setter # se o usuario quiser trocar o nome do titular da conta o sistema irá pedir a senha
    def nome(self, novo_nome:str=None):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            if len(novo_nome) >= 3:
                self._titular = novo_nome
        else:
            print("Senha não confere, não podemos alterar nome!")

