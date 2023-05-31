from FIAP.Fase03.Capitulo08.lista_metodo import def_validacao

categoria_digitada = input("Digite a categoria de habilitação")

def_validacao.categorias.append('ESPECIAL')
def_validacao.validar_categoria(categoria_digitada)