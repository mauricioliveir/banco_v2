from datetime import datetime

# Constantes
AGENCIA = "0001"
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500
MSG_CONTA_NAO_ENCONTRADA = "Conta não encontrada!"
MSG_INFORME_CPF = "Informe o CPF do cliente: "

def depositar(saldo, valor, extrato):
    """
    Realiza um depósito na conta.

    :param saldo: Saldo atual da conta.
    :param valor: Valor a ser depositado.
    :param extrato: Extrato atual da conta.
    :return: Saldo e extrato atualizados.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque na conta.

    :param saldo: Saldo atual da conta.
    :param valor: Valor a ser sacado.
    :param extrato: Extrato atual da conta.
    :param limite: Limite máximo de valor por saque.
    :param numero_saques: Número de saques já realizados.
    :param limite_saques: Limite máximo de saques permitidos.
    :return: Saldo, extrato e número de saques atualizados.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.

    :param saldo: Saldo atual da conta.
    :param extrato: Extrato atual da conta.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes):
    """
    Cria um novo cliente e o adiciona à lista de clientes.

    :param clientes: Lista de clientes existentes.
    """
    cpf = input("Informe o CPF (somente números): ")
    if any(cliente['cpf'] == cpf for cliente in clientes):
        print("CPF já cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = {
        'logradouro': input("Informe o logradouro: "),
        'numero': input("Informe o número: "),
        'bairro': input("Informe o bairro: "),
        'cidade': input("Informe a cidade: "),
        'estado': input("Informe a sigla do estado: ")
    }

    clientes.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Cliente cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, clientes):
    """
    Cria uma nova conta para um cliente existente.

    :param agencia: Número da agência.
    :param numero_conta: Número da conta.
    :param clientes: Lista de clientes existentes.
    :return: Dicionário com os dados da conta criada.
    """
    cpf = input(MSG_INFORME_CPF)
    cliente = next((cliente for cliente in clientes if cliente['cpf'] == cpf), None)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'cliente': cliente,
        'saldo': 0,
        'extrato': "",
        'numero_saques': 0
    }
    print("Conta criada com sucesso!")
    return conta

def encontrar_conta_por_cpf(cpf, contas):
    """
    Encontra uma conta pelo CPF do cliente.

    :param cpf: CPF do cliente.
    :param contas: Lista de contas existentes.
    :return: Conta encontrada ou None se não existir.
    """
    return next((conta for conta in contas if conta['cliente']['cpf'] == cpf), None)

def processar_deposito(contas):
    """
    Processa a operação de depósito.

    :param contas: Lista de contas existentes.
    """
    cpf = input(MSG_INFORME_CPF)
    conta = encontrar_conta_por_cpf(cpf, contas)
    if not conta:
        print(MSG_CONTA_NAO_ENCONTRADA)
        return

    valor = float(input("Informe o valor do depósito: "))
    conta['saldo'], conta['extrato'] = depositar(conta['saldo'], valor, conta['extrato'])

def processar_saque(contas):
    """
    Processa a operação de saque.

    :param contas: Lista de contas existentes.
    """
    cpf = input(MSG_INFORME_CPF)
    conta = encontrar_conta_por_cpf(cpf, contas)
    if not conta:
        print(MSG_CONTA_NAO_ENCONTRADA)
        return

    valor = float(input("Informe o valor do saque: "))
    conta['saldo'], conta['extrato'], conta['numero_saques'] = sacar(
        saldo=conta['saldo'],
        valor=valor,
        extrato=conta['extrato'],
        limite=LIMITE_VALOR_SAQUE,
        numero_saques=conta['numero_saques'],
        limite_saques=LIMITE_SAQUES
    )

def processar_extrato(contas):
    """
    Processa a operação de exibição de extrato.

    :param contas: Lista de contas existentes.
    """
    cpf = input(MSG_INFORME_CPF)
    conta = encontrar_conta_por_cpf(cpf, contas)
    if not conta:
        print(MSG_CONTA_NAO_ENCONTRADA)
        return

    exibir_extrato(conta['saldo'], extrato=conta['extrato'])

def main():
    """
    Função principal que executa o sistema bancário.
    """
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[cc] Criar Conta
[q] Sair

=> """

    clientes = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            processar_deposito(contas)
        elif opcao == "s":
            processar_saque(contas)
        elif opcao == "e":
            processar_extrato(contas)
        elif opcao == "c":
            criar_cliente(clientes)
        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()