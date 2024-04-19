menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser Depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$: {valor:.2f}\n"

        else:
            print("A operação falhou! O valor informado é invalido")

    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))

        execedeu_saldo = valor > saldo

        execedeu_limite = valor > limite

        execedeu_saque = numero_saque > LIMITE_SAQUE

        if execedeu_saldo:
            print("Operação Falhou! Você não tem saldo o suficiente.")

        elif execedeu_limite:
            print("Operação Falhou! O valor de saque execede o limite da conta. ")

        elif execedeu_saque:
            print("Operação Falhou! Você execedeu o valor de saques diarios. ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saques R$: {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! o valor informado é invalido")

    elif opcao == "e":
        print("\n========== Extrato ============ ")
        print("Não foram realizada movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$: {saldo:.2f}")
        print("\n=============================== ")

    elif opcao == "q":
        break

    else:
        print("Operção invalida! Digite uma opção valida")
