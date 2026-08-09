'''from contabancaria import *
from rich import print, inspect
from time import sleep

def main():
    print("Criando a conta...")
    sleep(1)
    cc = ContaBancaria(111, 'Hugo', 1000)


    print("Realizando depósito...")
    sleep(1)
    cc.depositar(500)

    print("Realizando saque...")
    sleep(1)
    cc.saque('111',200)

    #cc.nome = 'Manoel' # trocar nome

    inspect(cc, private=True, methods=True)

if __name__ == '__main__':
    main()'''

from contabancaria import *
from rich import print, inspect
from time import sleep
from rich.panel import Panel

def main():
    cc = None
    print("[blue]  Bem vindo  [/]".center(50, "-"))
    sleep(1)
    while True:

        caixa = Panel("""
0 = Sair
1 = Criar conta bancaria
2 = Sacar
3 = Depositar
4 = Mudar nome do titular da conta
5 = Ver saldo
""", title="Comandos", width=40)
        print(caixa)
        comando = int(input("Digite sua opção -> "))
        match comando:
            case 0:
                print("[green]Saindo do programa...[/]")
                print("[blue]  Volte sempre  [/]".center(50, "-"))
                break
            case 1:
                if cc is None:
                    print("[yellow]Conta criada com sucesso![/]")
                else:
                    cc = ContaBancaria(111, "Hugo", 10_000, 'casagrande')
            case 2:
                if cc is None:
                    print("[red]Primeiro crie a conta[/]!")
                    return
                valor = float(input("Informe o valor do saque?"))
                cc.saque(valor)
            case 3:
                valor = float(input("Informe o valor do deposito?"))
                cc.deposito(valor)
            case 4:
                cc.nome = str(input("Informe o novo nome do titular da conta?"))
            case 5:
                if cc is None:
                    print("[red]Primeiro crie a conta[/]!")
                    return
                else:
                    1print(f"[green]Saldo atual: R$:{cc.saldo:.2f}[/]")
        #inspect(cc, private=True, methods=True)

if __name__ == '__main__':
    main()