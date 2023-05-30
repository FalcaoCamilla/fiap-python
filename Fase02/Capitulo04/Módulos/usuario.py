import calculadora
###importação de funções específica do módulo calculadora.py
##from calculadora import somar, subtrair

valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

soma = calculadora.somar(valor1, valor2)

print("A soma é {}".format(soma))