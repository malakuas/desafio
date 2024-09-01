menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        deposito = int(input("Deposite o valor desejado\n"))
        
        if deposito > 0:
            print("deposito feito com sucesso")
            saldo += deposito
            extrato += f"Depósito; R$ {deposito:.2f}\n"
        
        else:
            print("opção inválida\n")

    
    elif opcao == "s":
        deposito = float(input("Qual o valor do saque: "))
        excedeu_saldo = deposito > saldo
        excedeu_limite = deposito > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem mais dinheiro para sacar\n")
        
        elif excedeu_limite:
            print("você não pode sacar além do limite\n")
        
        elif excedeu_saques:
            print("você não tem mais saques hoje\n")
        
        elif saldo > 0:
            saldo -= deposito
            extrato = f"Saque: R$ {deposito:.2f}\n"
            numero_saques += 1

        else:
            print("falha, o valor informado é invalido\n")

    elif opcao == "e":
        print("==============EXTRATO==============\n")
        print("Não foram realizadas transações.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("===================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Escolha uma opção válida\n")