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

    if opcao == "1":
        valor = float(input("Informe o valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! \nO valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Operação falhou! \nSaldo suficiente.")
        elif valor > limite:
            print("Operação falhou! \nO saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! \nNúmero de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação falhou! \nO valor é inválido.")

    elif opcao == "3":
        print("\n--------------- EXTRATO ---------------")
        print("Não houve movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n-----------------------------------------")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, tente novamente.")
