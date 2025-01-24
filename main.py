menu = """

------------Menu------------

(1) - Depositar
(2) - Sacar
(3) - Visualizar Extrato
(0) - Sair

"""
saldo = 0
limite = 500
saques_efetuados = 0
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
            print("Voce depositou R$ %.2f.\n", valor_deposito)
        else:
            print("Valor inserido invalido.")
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
                else:
                    print("Saldo insuficiente.\n")
            else:
                print("Valor inserido maior que o limite. \n")
        else:
            print("Limite diario de saques atingido. \n")
    # elif (selecao_usuario == 3):
    #sair
    elif (selecao_usuario == 0):
        print("Agradecemos por utilizar nossos serviços. Ate a proxima! \n")
        break
    else:
        print("Numero inserido invalido. Tente novamente \n")

    