menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 100
limite = 500
extrato = ""
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito= float(input("Quanto deseja depositar? "))

        if deposito > 0:
            saldo +=deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print (f"Depósito de R$ {deposito:.2f} realizado!")
        else:
            print("Valor inválido, por favor insira um valor maior que zero!")
    
    elif opcao == "s":
        if LIMITE_SAQUES >0:
            saque = float(input("Qual valor deseja sacar?"))
            if saque > limite:
                print("Valor acima do permitido, saque máximo de R$500,00")
            else:
                if saldo < saque:
                    print ("Saldo insuficiente")
                else: 
                    saldo -= saque
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    print (f"Saque de R$ {saque:.2f} realizado!")
                    LIMITE_SAQUES = LIMITE_SAQUES-1
        else:
            print ("Limites de saques atingido")
    
    elif opcao == "e":
        print("\n ######## EXTRATO ########")
        if extrato == "":
            print ("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###########################\n")
    
    elif opcao == "q":
        break
    else:
        print ("Opção inválida, tente novamente")