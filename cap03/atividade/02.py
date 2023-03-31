segunda = int(input("Digite a quantidade de votos para segunda-feira: "))
terca = int(input("Digite a quantidade de votos para terça-feira: "))
quarta = int(input("Digite a quantidade de votos para quarta-feira: "))
quinta = int(input("Digite a quantidade de votos para quinta-feira: "))
sexta = int(input("Digite a quantidade de votos para sexta-feira: "))

votos = {"Segunda-feira": segunda, "Terça-feira": terca, "Quarta-feira": quarta, "Quinta-feira": quinta, "Sexta-feira": sexta}

print(votos.get())