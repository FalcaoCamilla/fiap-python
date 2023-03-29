print('Compra de pacotes com desconto!')

valor_bruto = float(input("Informe o valor do pacote"))
categoria = input("Qual será a categoria dos assentos?")
quantidade_viajantes = 0

if categoria.upper() == "ECONÔMICA" or categoria.upper() == "EXECUTIVA" or categoria.upper() == "PRIMEIRA CLASSE":
    quantidade_viajantes = int(input("Quantos viajantes serão incluídos?"))
    validador = True
    desconto = 0
else:
    print("Categoria inválida")
    validador = False

if categoria.upper() == "ECONÔMICA":
    if quantidade_viajantes == 2:
        desconto = 3
    elif quantidade_viajantes == 3:
        desconto = 4
    elif quantidade_viajantes >= 4:
        desconto = 5
elif categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 2:
        desconto = 5
    elif quantidade_viajantes == 3:
        desconto = 7
    elif quantidade_viajantes >= 4:
        desconto = 8
elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 2:
        desconto = 10
    elif quantidade_viajantes == 3:
        desconto = 15
    elif quantidade_viajantes >= 4:
        desconto = 20

if validador:
    valor_final = valor_bruto - (valor_bruto * (desconto / 100))
    valor_medio = valor_final / quantidade_viajantes
    print("RESUMO DA COMPRA: \n Classe {} para {} viajantes. \n Valor da compra: {} \n Descontos aplicados: -{}% \n "
          "Valor com desconto: {} \n Valor médio por viajante: {}".format(categoria, quantidade_viajantes, valor_bruto,
                                                                          desconto, valor_final, valor_medio))
