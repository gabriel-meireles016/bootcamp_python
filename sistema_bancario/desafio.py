import textwrap as tw

def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [0] Sair
    => """
    return input(tw.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R${valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou. Valor inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    caso1 = valor > saldo
    caso2 = valor > limite
    caso3 = numero_saques >= limite_saques
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
    
    return saldo, extrato

def puxar_extrato(saldo,/,*, extrato):
    print("Extrato Bancário")
    print("Sem transações." if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")

def criar_usuario(usuario):
    nome = input("Informe o nome: ")
    cpf = input("Informe o CPF (Somente numeros): ")
    nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o CEP (Somente numeros): ")
    
    usuario.append({"nome": nome, "CPF": cpf, "data_nascimento": nasc, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def criar_conta(ag, num_conta, usuario):
    return {"agencia": ag, "numero_conta": num_conta, "usuario": usuario}

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuario = []
    conta = []
    

    while True:

        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar()
        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == 3:
            puxar_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            criar_usuario(usuario)
        elif opcao == 5:
            num_conta = len(conta) + 1
            conta = criar_conta(AGENCIA, num_conta, usuario)

            if conta:
                conta.append(conta)
        elif opcao == 0:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()