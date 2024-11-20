def imprimir_elementos(lista):
    for elemento in lista:
        if type(elemento) is list:
            imprimir_elementos(elemento)
        else:
            print(elemento)

lista = ["a", "b", ["c", "d", ["e", "f"], "g"], "h"]
imprimir_elementos(lista)
