from hashlib import sha256
from pwinput import pwinput

class Cadastro:
    def __init__(self):
        self.pessoa = []# Lista onde serão armazenados os nomes

        senha = pwinput("Cadastre uma senha?")#Senha inicial do cadastro

        self.senha = sha256(senha.encode()).hexdigest()#Transforme a senha em hash

    def cadastrar_pessoa(self):
        senha = pwinput("Digite a senha:")#Pede a senha para permitir o cadastro

        if sha256(senha.encode()).hexdigest() == self.senha: #Verifica a senha se esta correta
            nome = input("Digite o nome da pessoa:")

            self.pessoa.append(nome)#Adiciona o nome na lista

            print(f"{nome} cadastrado(a) com sucesso!!!")

        else:
            print("Senha incorreta!!!")

    def ver_pessoa(self):
        senha = pwinput("Digite a senha:")#Verifica senha digitada


        if sha256(senha.encode()).hexdigest() == self.senha:  # Verifica a senha se esta correta

            if self.pessoa:
                print("Pessoa cadastrada")

                for pessoa in self.pessoa:
                    print(f"{pessoa}")

            else:
                print("Não foi cadastrado(a)")

        else:
            print("Senha Incorrera!!!")

    def alterar_senha(self):
        senha = pwinput("Digite a senha:")

        if sha256(senha.encode()).hexdigest() == self.senha:
            nova_senha = pwinput("Digite a nova senha:")

            self.senha = sha256(nova_senha.encode()).hexdigest()#Guarda a nova senha
            print(f"{nova_senha} adicionada com sucesso!!!")

        else:
            print("Senha incorreta!!!")


