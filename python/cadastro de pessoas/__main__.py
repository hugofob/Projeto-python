from rich.panel import Panel
from rich import print
from cadastro import *
from time import sleep

def main():
    c = Cadastro()
    while True:
        caixa = Panel("""
0 = Sair
1 = Cadastrar Pessoa
2 = Ver Pessoa Cadastrada
3 = Alterar Senha
        """, title="Comandos", width=30)
        print(caixa)

        comando = str(input(f"\nDigite sua Opção"))

        match comando:
            case '0':
                sleep(1)
                print("Encerrando o Programa...")
                break
            case '1':
                c.cadastrar_pessoa()
            case '2':
                c.ver_pessoa()
            case '3':
                c.alterar_senha()
            case _:
                print("\nOpção inválida!")
        print("\n" * 5)

if __name__ == '__main__':
    main()