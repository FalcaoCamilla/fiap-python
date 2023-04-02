nota_par = 0
nota_impar = 0
media_par = 0
media_impar = 0

for i in range (0, 51, 1):
    if i%2 == 0:
        nota_par += float(input("Você está digitando as notas dos alunos pares\nPor favor, insira a nota do aluno de número {i}\n"))
    else:
        nota_impar += float(input("Você está digitando as notas dos alunos ímpares\nPor favor, insira a nota do aluno de número {i}\n"))

media_par = nota_par/25
media_impar = nota_impar/25
print(f"A média da metade par é {media_par}\n A média da metade ímpar é {media_impar}")
