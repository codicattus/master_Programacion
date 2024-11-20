from typing import Any

lista: list[Any] = []
texto = ""

if type(lista) is list:
    print("lista es un objeto de la clase list")
else:
    print(f"lista es un objetos de la clase {type(lista)}")

# Resultado :
#
# lista es un objeto de la clase list

if type(texto) is list:
    print("Lista es un objeto de la clase list")
else:
    print(f"lista es un objetos de la clase {type(texto)}")

# Resultado :
#
# lista es un objetos de la clase <class 'str'>