print('Verificador de saúde cardíaca')

nome = input("Informe o seu nome \n")
bpm = float(input("Informe o número de batimentos cardíacos por minuto\n"))
idade = int(input("Informe sua idade\n"))

abaixo = '{}, sua frequência carrdíaca está abaixo da faixa adequada'.format(nome)
dentro = '{}, sua frequência cardíaca está dentro da faixa adequada'.format(nome)
acima = '{}, sua frequência cardíaca está acima da faixa adequada'.format(nome)

if idade <= 2:
    if bpm < 120:
        print(abaixo)
    elif 120 <= bpm <= 140:
        print(dentro)
    else:
        print(abaixo)
elif 8 <= idade <= 17:
    if bpm < 80:
        print(abaixo)
    elif 80 <= bpm <= 100:
        print(dentro)
    else:
        print(acima)
elif 18 <= idade <= 59:
    if bpm < 70:
        print(abaixo)
    elif 70 <= bpm <= 80:
        print(dentro)
    else:
        print(acima)
else:
    if bpm < 50:
        print(abaixo)
    elif 50 <= bpm <= 60:
        print(dentro)
    else:
        print(acima)