# *args - Permite pasar un número variable de argumentos no nombrados a una función. 
# Dentro de la función, *args se comporta como una tupla que contiene todos los argumentos adicionales.

def sum_alls(*args : int) -> int:
    return sum(args)

result = sum_alls(4, 5, 9, 5, 7)
print(result)

# Resultado :
#
# 30

# *kwargs - permite pasar un número variable de argumentos nombrados a una función. 
# Dentro de la función, **kwargs se comporta como un diccionario que contiene todos los argumentos adicionales con nombre.

def show_info(**kwargs: dict) -> None:
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
    print(f"{"*" * 20}")
show_info(nombre="Juan", edad=18, ciudad="Barcelona")
show_info(nombre="María", edad=20, ciudad="Madrid")
show_info(nombre="Luis", ciudad="Madrid")

def operations(num: int, *args: int) -> int:
    return num * sum(args)

print(operations(4, 2, 3))

# Resultado:
# 20