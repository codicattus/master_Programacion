# *args - Permite pasar un número variable de argumentos no nombrados a una función. 
# Dentro de la función, *args se comporta como una tupla que contiene todos los argumentos adicionales.

def sum_alls(*args : int) -> int:
    """ Suma todos los argumentos enteros proporcionados y devuelve el resultado.

    Esta función acepta un número variable de argumentos enteros y devuelve su suma total. :param args: Números enteros a sumar. 
    :type args: int 
    :return: La suma de todos los argumentos proporcionados. 
    :rtype: int 
    """
    return sum(args)

result = sum_alls(4, 5, 9, 5, 7)
print(result)

# Resultado :
#
# 30

# *kwargs - permite pasar un número variable de argumentos nombrados a una función. 
# Dentro de la función, **kwargs se comporta como un diccionario que contiene todos los argumentos adicionales con nombre.

def show_info(**kwargs: dict) -> None:
    """ Muestra información pasada como argumentos de palabra clave y la imprime en un formato legible. 
    
    Esta función acepta un número variable de argumentos de palabra clave (kwargs) y los imprime en un formato "clave: valor". Después de imprimir todos los pares clave-valor, imprime una línea de asteriscos para separar las llamadas a la función. 
    :param kwargs: Argumentos de palabra clave que representan la información a mostrar. 
    :type kwargs: dict 
    :return: None 
    """
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