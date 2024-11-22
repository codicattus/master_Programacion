def exponential(num:int, expo:int = 2) ->int:
    """Calcula el valor de un número elevado a una potencia.
    Si no se proporciona el exponente, devuelve el cuadrado del número.
    :param num: El número base a elevar.
    :type num: int
    :param expo: La potencia a la que se debe elevar el número. Por defecto es 2.
    :type expo: int, opcional
    :return: El resultado de `number` elevado a `exp`.
    :rtype: int
    :raises ValueError: Si `number` o `exp` no son números enteros.
    """
    return num ** expo


number = int(input("Introduce un número: "))
exp = input("Introduce el exponente: ")
exponent :int = int(exp) if exp else 2
print(exponential(number, exponent))