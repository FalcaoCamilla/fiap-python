#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#convertendo o dicionário para uma string o formato json
final = json.dumps(contatos)

#exibindo a string convertida
print(final)

final = json.dumps(contatos, indent=4)
print(final)

#criando um arquivo
arquivo = open("c:\arquivos\agenda.json", "w")

#escrevendo o JSON dentro do arquivo
arquivo.write(final)

#fechando o arquivo
arquivo.close()