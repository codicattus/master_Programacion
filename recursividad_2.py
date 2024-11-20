def imprimir_elementos(lista):
    for elemento in lista:
        if isinstance(elemento, list):
            imprimir_elementos(elemento)
        else:
            print(elemento)

# Ejemplo de uso
lista = ["a", "b", ["c", "d", ["e", "f"], "g", ["h", "i"]], "j"]
imprimir_elementos(lista)
