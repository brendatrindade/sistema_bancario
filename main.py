menu = """
------------Menu------------

(1) - Depositar
(2) - Sacar
(3) - Visualizar Extrato
(4) - Visualizar Saldo
(5) - Cadastrar Cliente
(6) - Cadastrar Conta
(7) - Consultar Contas Cadastradas
(0) - Sair
"""
saldo = 0
limite = 500
saques_efetuados = 0
depositos_efetuados = 0
LIMITE_SAQUES_DIARIO = 3
extrato = {}
usuarios = {}
contas = {}
AGENCIA = "0001"

num_conta = 0

def cadastrar_usuario(usuarios):
    print("----------Cadastro----------\n")
    cpf = input("Digite o seu CPF (apenas numeros): ")
    if not(cpf in usuarios):
        nome = input("Nome completo: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        telefone = input("Telefone: ")
        logradouro = input("------Endereco------\nLogradouro: ")
        numero = input("Numero: ")
        cidade = input("Cidade: ")
        sigla_estado = input("Sigla do Estado: ")
        usuarios.update({cpf: {
            "nome": nome.title(),  
            "data de nascimento": data_nascimento, 
            "telefone": telefone, 
            "endereco": {
                "logradouro": logradouro.title(), 
                "numero": numero, 
                "cidade/estado": (f"{cidade.title()}/{sigla_estado.upper()}")} }})

        print(f'Cadastro efetuado com sucesso!\nNome: {usuarios[cpf]["nome"]} - CPF: {cpf}\n')
    else:
        print("CPF ja cadastrado")

def cadastrar_conta(contas):
    global num_conta
    print("----Cadastrar Nova Conta----\n")
    cpf = input("Digite o seu CPF (apenas numeros): ")

    if (cpf in usuarios.keys()):
        num_conta += 1
        conta= (f"000.00{num_conta}")

        if cpf in contas.keys():
            contas[cpf]["numero da conta"].append(conta)
        else:
            contas.update( {cpf: {
            "agencia": AGENCIA, 
            "numero da conta": [conta], 
            "titular": usuarios[cpf]["nome"] }})

        print(f'Conta criada com sucesso!\n Titular: {contas[cpf]["titular"]} - CPF: {cpf} \nAgencia: {AGENCIA} - Numero da Conta: {contas[cpf]["numero da conta"]}')
    else:
        print("CPF nao cadastrado, cadastre-se para criar uma conta")

def visualizar_contas(contas):
    cpf = input("Digite o seu CPF (apenas numeros): ")
    print("-------Contas Cadastradas-------\n")
    print(f'Titular: {(contas[cpf]["titular"])} - CPF: {cpf} \nAgencia: {AGENCIA} - Numero da Conta: {contas[cpf]["numero da conta"]}')

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

    #cadastro cliente
    elif (selecao_usuario == 5):
        cadastrar_usuario(usuarios)
    #cadastro conta
    elif (selecao_usuario == 6):
        cadastrar_conta(contas)
    #visualizar contas cadastradas
    elif (selecao_usuario == 7):
        visualizar_contas(contas)
    #sair
    elif (selecao_usuario == 0):
        print("\nAgradecemos por utilizar nossos serviços. Ate a proxima! \n")
        break
    else:
        print("\nNumero inserido invalido. Tente novamente \n")
