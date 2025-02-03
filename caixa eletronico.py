menu = '''[d] depositar
[s] sacar
[e] extrato
[q] sair '''
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3
valores_saque = []
valores_deposito = []  # Lista para armazenar os valores depositados

while True:
    opcao = input(menu)
    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: "))
        saldo += deposito
        extrato += f"Depósito de R${deposito}\n"
        valores_deposito.append(deposito)  # Adicionando valor à lista de depósitos
    elif opcao == "s":
        if numero_saque >= limite_saque:
            print("Limite de 3 saques diários atingidos, não é mais possível sacar hoje.")
            break
        valor_saque = float(input("Quanto deseja sacar: "))
        if valor_saque > 500:
            print("Limite máximo de 500 R$ por saque ultrapassado, não será possível sacar esse valor.")
            break
        if sum(valores_saque) + valor_saque > saldo:
            print(f"Seu saldo é de {saldo} R$")
            print("Saldo insuficiente, não será possível realizar o saque.")
            break
        numero_saque += 1
        saldo -= valor_saque
        valores_saque.append(valor_saque)
        extrato += f"Saque de R${valor_saque}\n"
    elif opcao == "e":
        print(f"Seu extrato é:\n{extrato}Saldo atual: R${saldo}")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção")

print(f"Seu saldo é de {saldo} R$")
print(f"Você realizou {numero_saque} saques")
print("Histórico de Saques:")
for valor in valores_saque:
    print(f"- R${valor}")

print("Histórico de Depósitos:")
for valor in valores_deposito:
    print(f"- R${valor}")