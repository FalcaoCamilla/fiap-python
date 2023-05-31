def validar_categoria(categoria_usuario):
    if categoria_usuario.upper() in categorias:
        print("Categoria válida!")
    else:
        print("Categoria inválida!")
categorias=["A", "B", "C", "D", "E"]
