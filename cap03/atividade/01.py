#esboço da questão -- antes da refatoração
assinatura = input("Por favor, informe o tipo de assinatura do cliente.")
faturamento = float(input("Insira o valor do faturamento anual do cliente."))
porcentagem = 0

while assinatura.upper() != "BASIC" or assinatura.upper() != "SILVER" or assinatura.upper() != "GOLD" or assinatura.upper() != "PLATINUM":
    assinatura = input("Por favor, informe um tipo válido de assinatura do cliente.")
#nesse caso, a condição do while loop sempre será verdadeira, 
#pois uma string sempre será diferente de três outras strings.
#posso trocar o or pelo and ou utilizar o not in

if assinatura.upper() == "BASIC":
    porcentagem = 30
elif assinatura.upper() == "SILVER":
    porcentagem = 20
elif assinatura.upper() == "GOLD":
    porcentagem = 10
elif assinatura.upper() == "PLATINUM":
    porcentagem = 5

#descontos = {"BASIC": 30, "SILVER": 20, "GOLD": 10, "PLATINUM": 5}
#porcentagem = descontos.get(assinatura.upper(), 0)
#O método get do dicionário retorna o valor correspondente à chave, 
#ou 0 se a chave não existir no dicionário.

bonus = faturamento * (porcentagem/100)
print(f'O cliente deverá pagar um valor de R${bonus}')