# Menu de opções para o usuário
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

# Inicialização de variáveis
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite de saque por transação
extrato = ""  # Histórico de transações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Número máximo de saques permitidos por dia

# Loop principal do programa
while True:
    opcao = input(menu) # Exibe o menu e captura a opção do usuário

    # Depósito
    if opcao == "1":
        valor = float(input("Informe o valor para depósito: "))
        if valor > 0: # Verifica se o valor do depósito é positivo
            saldo += valor # Atualiza o saldo
            extrato += f"Depósito: R$ {valor:.2f}\n" # Adiciona ao extrato
        else:
            print("Operação falhou! \nO valor informado é inválido.") # Mensagem de erro para valor inválido

    # Saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo: # Verifica se o valor do saque excede o saldo
            print("Operação falhou! \nSaldo suficiente.")
        elif valor > limite: # Verifica se o valor do saque excede o limite permitido
            print("Operação falhou! \nO saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES: # Verifica se o número de saques permitidos foi excedido
            print("Operação falhou! \nNúmero de saques excedido.")
        elif valor > 0: # Verifica se o valor do saque é positivo
            saldo -= valor # Atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n" # Adiciona ao extrato
            numero_saques += 1 # Incrementa o contador de saques
            
        else:
            print("Operação falhou! \nO valor é inválido.")  # Mensagem de erro para valor inválido

    # Extrato
    elif opcao == "3":
        print("\n--------------- EXTRATO ---------------")
        print("Não houve movimentações." if not extrato else extrato) # Exibe o extrato ou mensagem de ausência de movimentações
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n-----------------------------------------")

    # Sair
    elif opcao == "0":
        break  # Encerra o loop e finaliza o programa

    # Opção inválida
    else:
        print("Operação inválida, tente novamente.")  # Mensagem de erro para opção inválida