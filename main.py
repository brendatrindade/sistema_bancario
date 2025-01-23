menu = """

----Olá! Seja bem-vindo(a)----

Pressione:

(1) - Depositar
(2) - Sacar
(3) - Visualizar Extrato
(0) - Sair

"""
saldo = 0
limite = 500
saques_efetuados = 0
LIMITE_SAQUES_DIARIO = 3

while (1):
    selecao_usuario = int(input("Digite o numero da operacao que deseja realizar: "))
    #deposito
    if (selecao_usuario == 1):
        valor_deposito = int(input("Digite o valor que deseja depositar: "))
        saldo += valor_deposito
        print("Voce depositou R$ %.2f.\n", valor_deposito)
    # elif (selecao_usuario == 2):
    # elif (selecao_usuario == 3):
    # elif (selecao_usuario == 0):
    # else:
    