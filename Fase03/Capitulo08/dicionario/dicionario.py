#criando um dicionário com dados
dicionário = {"Yoda": "Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker": "Cavaleiro Jedi", "R2-D2": "Dróide", "Dex": "Balconista"}
#exibindo o valor associado a uma chave específica
print(dicionário["R2-D2"])
#exibindo todos os valores em um dicionário
for valor in dicionário.values():
    print(valor)
for chave in dicionário.keys():
    print(chave)
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
#removendo o item cuja chave é R2-D2
dicionário.pop("R2-D2")
#removendo o último item
dicionário.popitem()
#removendo todos os itens
dicionário.clear()

#criando um dicionário vazio
dicionário2 = {}
#incluindo dados no dicionário
dicionário2["André David"] = "Professor"
#Pedindo para o usuário incluir dados no dicionário
nova_chave = input("Informe o nome do colaborador da FIAP")
novo_valor = input("Informe a função do colaborador da FIAP")
dicionário2[nova_chave] = novo_valor
#exibindo o dicionário completo
for chave, valor in dicionário2.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))