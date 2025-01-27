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

def depositar(saldo_conta, depositos_efetuados, extrato_conta, /):
    valor_deposito = int(input("Digite o valor que deseja depositar: "))
    if (valor_deposito > 0):
        saldo_conta += valor_deposito
        depositos_efetuados += 1
        key_deposito = (f"deposito {depositos_efetuados}")
        extrato_conta.update({key_deposito: valor_deposito})
        print("\nVoce depositou R$ %.2f \n" % valor_deposito)
    else:
        print("\nValor inserido invalido.\n")

    return saldo_conta, depositos_efetuados

def sacar(*, saldo_conta, saques_efetuados, limite_por_saque, extrato_conta):
    if (saques_efetuados < LIMITE_SAQUES_DIARIO):
        valor_saque = int(input("Digite o valor que deseja sacar: "))
        if (valor_saque < limite_por_saque):
            if (valor_saque <= saldo_conta):
                saldo_conta -= valor_saque
                saques_efetuados +=1
                key_saque = (f"saque {saques_efetuados}")
                extrato_conta.update({key_saque: valor_saque})
                print("\nVoce sacou R$ %.2f \n" % valor_saque)
            else:
                print("\nSaldo insuficiente.\n")
        else:
            print("\nValor inserido maior que o limite. \n")
    else:
        print("\nLimite diario de saques atingido.\n")
                
    return saldo_conta, saques_efetuados

def exibir_extrato(saldo_conta, /,*, extrato_conta):
    print("\nExtrato das operações realizadas recentemente: \n")
    for key in extrato_conta:
        print(key + ": R$ %.2f \n" % extrato_conta.get(key))
    exibir_saldo(saldo_conta)

def exibir_saldo(saldo_conta):
    print("\nSaldo disponivel: R$ %.2f\n" % saldo_conta)

while (1):
    print(menu)
    selecao_usuario = int(input("Digite o numero da operacao que deseja realizar: "))
    #deposito
    if (selecao_usuario == 1):
        saldo, depositos_efetuados = depositar(saldo, depositos_efetuados, extrato)

    #saque
    elif (selecao_usuario == 2):
        saldo, saques_efetuados = sacar(saldo_conta=saldo, saques_efetuados=saques_efetuados, limite_por_saque=limite, extrato_conta=extrato)

    #extrato
    elif (selecao_usuario == 3):
        exibir_extrato(saldo, extrato_conta=extrato)

    #saldo
    elif (selecao_usuario == 4):
        exibir_saldo(saldo)

    #sair
    elif (selecao_usuario == 0):
        print("\nAgradecemos por utilizar nossos serviços. Ate a proxima! \n")
        break
    else:
        print("\nNumero inserido invalido. Tente novamente \n")
