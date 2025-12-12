menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
clientes=[]
contas=[]
conta=0


def deposito(valor,extrato,/):
    
    if valor > 0:
        global saldo
        saldo += valor
        resultadoSaldo= f"Saldo: R$ {saldo:.2f}\n"
        extrato = f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return print(resultadoSaldo, extrato)

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
        
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
        resultadoSaldo= f"Saldo: R$ {saldo:.2f}\n"
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return print(resultadoSaldo, extrato)

def extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return
def cadastrarUsuario():
     
    nome = str(input("Informe o nome: "))
    cpf = str(input("Informe o cpf: "))
    nascimento = str(input("Informe a data de nascimento: "))
    endereco = str(input("Informe o endereço: "))
    novo_cliete=(nome,cpf,nascimento,endereco)
    print(novo_cliete)
    global clientes
    
    for cliente in clientes:
        if cpf in cliente:
            print ("Usuário já cadastrado")
            return clientes
            
    clientes.append(novo_cliete)
            

    return clientes

def cadastrarContaCorrente():
    agencia="0001"
    global conta
    
    cpf1 = str(input("Informe o cpf: "))
    global clientes
    for cliente in clientes:
        if cpf1  in cliente:
            conta=conta+1
            contas.append((agencia,cpf1,conta))
            return contas

              
    print ("cadastrar usuário")

    return contas

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))
        deposito(valor,extrato)
        cadastrarContaCorrente()
        print (contas)

        
        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)

        

    elif opcao == "e":
        extrato(saldo,extrato=extrato)
        cadastrarUsuario()
        print (clientes)
        
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



