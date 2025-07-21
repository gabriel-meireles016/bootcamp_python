menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}\n"
        else:
            print("Operação falhou. Valor inválido.")
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        caso1 = valor > saldo
        caso2 = valor > limite
        caso3 = numero_saques >= LIMITE_SAQUES
        caso4 = valor > 0

        if caso1:
            print("Operação falhou. Valor maior que o saldo.")
        elif caso2:
            print("Operação falhou. Valor de saque maior que o limite.")
        elif caso3:
            print("Operação falhou. Limite de saques alcançado.")
        elif caso4:
            saldo -= valor
            extrato += f"Saque de R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou. Valor inválido.")
    elif opcao == 3:
        print("Extrato Bancário")
        print("Sem transações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")