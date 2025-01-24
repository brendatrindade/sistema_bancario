menu = """
------------Menu------------

(1) - Depositar
(2) - Sacar
(3) - Visualizar Extrato
(4) - Visualizar Saldo
(0) - Sair
"""
saldo = 0
limite = 500
saques_efetuados = 0
depositos_efetuados = 0
LIMITE_SAQUES_DIARIO = 3
extrato = {}

while (1):
    print(menu)
    selecao_usuario = int(input("Digite o numero da operacao que deseja realizar: "))
    #deposito
    if (selecao_usuario == 1):
        valor_deposito = int(input("Digite o valor que deseja depositar: "))
        if (valor_deposito > 0):
            saldo += valor_deposito
            depositos_efetuados += 1
            key_deposito = (f"deposito {depositos_efetuados}")
            extrato.update({key_deposito: valor_deposito})
            print("\nVoce depositou R$ %.2f \n" % valor_deposito)
        else:
            print("\nValor inserido invalido.\n")
    #saque
    elif (selecao_usuario == 2):
        if (saques_efetuados < LIMITE_SAQUES_DIARIO):
            valor_saque = int(input("Digite o valor que deseja sacar: "))
            if (valor_saque < limite):
                if (valor_saque <= saldo):
                    saldo -= valor_saque
                    saques_efetuados +=1
                    key = (f"saque {saques_efetuados}")
                    extrato.update({key: valor_saque})
                    print("\nVoce sacou R$ %.2f \n" % valor_saque)
                else:
                    print("\nSaldo insuficiente.\n")
            else:
                print("\nValor inserido maior que o limite. \n")
        else:
            print("\nLimite diario de saques atingido.\n")
    #extrato
    elif (selecao_usuario == 3):
        print("\nExtrato das operações realizadas recentemente: \n")
        for k in extrato:
            print(k + ": R$ %.2f \n" % extrato.get(k))
        print("Saldo disponivel: R$ %.2f\n" % saldo)
    #saldo
    elif (selecao_usuario == 4):
        print("\nSaldo disponivel: R$ %.2f\n" % saldo)
    #sair
    elif (selecao_usuario == 0):
        print("\nAgradecemos por utilizar nossos serviços. Ate a proxima! \n")
        break
    else:
        print("\nNumero inserido invalido. Tente novamente \n")
