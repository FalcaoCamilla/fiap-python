# usando a função open para criar um objeto do tipo arquivo
arquivo = open(r"c:\users\falcao\downloads\arquivo_de_texto.txt")

# verificando o tipo do objeto arquivo
print(type(arquivo))
# printar o conteúdo do arquivo
print(arquivo.read())
# printar linha do arquivo, em ordem
print(arquivo.readline())
# exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)

# passando o conteúdo do arquivo para uma lista
linhas_do_arquivo = arquivo.readlines()
# comprovando o tipo do objeto linhas_do_arquivo
print("Ei! Eu consegui transformar meu arquivo em uma {} ".format(type(linhas_do_arquivo)))
# colocando a lista em ordem alfabética
linhas_do_arquivo.sort()
# exibindo nossa lista, agora em ordem alfabética
print(linhas_do_arquivo)

# criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"
# usando a função open para criar um objeto do tipo novoArquivo
novoArquivo = open(r"c:\users\falcao\downloads\novo_arquivo.txt", "w")
# escrevendo o conteúdo da variável conteudo dentro do arquivo
novoArquivo.write(conteudo)
#fechando o arquivo
novoArquivo.close()