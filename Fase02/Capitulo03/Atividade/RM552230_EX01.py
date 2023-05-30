assinatura = input("Por favor, informe o tipo de assinatura do cliente.")
porcentagem = 0

while assinatura.upper() not in ["BASIC", "SILVER", "GOLD", "PLATINUM"]:
    assinatura = input("Por favor, informe um tipo válido de assinatura do cliente.")

faturamento = float(input("Insira o valor do faturamento anual do cliente."))

descontos = {"BASIC": 30, "SILVER": 20, "GOLD": 10, "PLATINUM": 5}
porcentagem = descontos.get(assinatura.upper(), 0)

bonus = faturamento * (porcentagem/100)
print(f'O cliente deverá pagar um valor de R${bonus:.2f}')


