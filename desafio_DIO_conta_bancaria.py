menu = """\n
=======================MENU==============================

Bem-vindo a sua Conta Bancária!

Por favor, para avançar selecione uma das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Digite sua opção a baixo:
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\nInforme o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\n Operação realizada com sucesso! O valor de R$ {valor:.2f} foi depositado a sua conta.") 

        else:
            print("\n Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\n Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\n Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n Saque realizado com sucesso! O valor de R$ {valor:.2f} foi sacado da sua conta.") 

        else:
            print("\n Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Nenhuma movimentação realizada até o momento." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("\nObrigado por usar nossos serviços. Tenha um Bom Dia!\n")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
