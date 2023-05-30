
playstation = 0
xbox = 0
nintendo = 0
ganhador = ""
frase = "O ganhador foi {} com {} votos"

for i in range (5):
    menu = int(input("Qual console você prefere? \n 1. Playstation \n 2. Xbox \n 3. Nintendo \n"))
    match menu:
        case 1:
            playstation += 1
        case 2:
            xbox += 1
        case 3:
            nintendo += 1
if playstation > xbox and playstation > nintendo:
    ganhador = "Playstation"
    print(frase.format(ganhador, playstation))
elif xbox > playstation and xbox > nintendo:
    ganhador = "Xbox"
    print(frase.format(ganhador, xbox))
elif nintendo > playstation and nintendo > xbox:
    ganhador = "Nintendo"
    print(frase.format(ganhador, nintendo))
else:
    print("Houve empate. Comece uma nova votação.")