segunda = int(input("Digite a quantidade de votos da segunda-feira: "))
terca = int(input("Digite a quantidade de votos da terça-feira: "))
quarta = int(input("Digite a quantidade de votos da quarta-feira: "))
quinta = int(input("Digite a quantidade de votos da quinta-feira: "))
sexta = int(input("Digite a quantidade de votos da sexta-feira: "))

votos = [segunda, terca, quarta, quinta, sexta]
maior_votos = max(votos)
dia_escolhido = ""

if maior_votos == segunda:
    dia_escolhido = "segunda-feira"
elif maior_votos == terca:
    dia_escolhido = "terça-feira"
elif maior_votos == quarta:
    dia_escolhido = "quarta-feira"
elif maior_votos == quinta:
    dia_escolhido = "quinta-feira"
else:
    dia_escolhido = "sexta-feira"

print("O dia escolhido foi:", dia_escolhido)