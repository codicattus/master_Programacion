def primos(dividendo: int | float) -> bool:
    """
    Determina si un número dado es primo. Un número primo es un número natural mayor que 1 que no tiene divisores positivos además de 1 y él mismo.

    Parámetros:
    dividendo (int): El número a comprobar si es primo.

    Retorna:
    bool: True si el número es primo, False en caso contrario.

    Ejemplos:
    >>> primos(7) True
    >>> primos(10) False
    >>> primos(1) False
    >>> primos(2) True
    """
    if dividendo <= 1:
        return False
    for divisor in range(2, dividendo):
        if dividendo % divisor == 0:
            return False
    else:
        return True


def fibonacci(cantidad_numeros: int = 0) -> list:
    """
    Genera una sucesión de Fibonacci hasta la cantidad de números especificados.

    Parámetros:
    cantidad_numeros (int): La cantidad de números en la sucesión de Fibonacci a generar. Si no se especifica, por defecto es 0 y retorna una lista vacía.

    Retorna:
    list: La sucesión de Fibonacci hasta la cantidad de números especificados. Si cantidad_numeros es 0, retorna una lista vacía. Si cantidad_numeros es 1, retorna una lista con un solo elemento [0].

    Ejemplos:
    >>> fibonacci(5) [0, 1, 1, 2, 3]
    >>> fibonacci(0) []
    >>> fibonacci(1) [0]
    """
    f0, f1 = 0, 1
    if not cantidad_numeros or cantidad_numeros == 0:
        return []
    if cantidad_numeros == 1:
        return [f0]
    sucesion_fibonacci = [f0, f1]
    while len(sucesion_fibonacci) < cantidad_numeros:
        sucesion_fibonacci.append(f0 + f1)
        f0, f1 = f1, f0 + f1
    return sucesion_fibonacci


def factorial(numero: int = 0) -> int:
    """
    Calcula el factorial de un número dado. El factorial de un número n (n!) es el producto de todos los enteros positivos desde 1 hasta n. Por ejemplo, el factorial de 5 es 5 * 4 * 3 * 2 * 1 = 120.

    Parámetros:
    numero (int): El número cuyo factorial se va a calcular. Por defecto es 0, y si es 0 o menor, retorna 0.
    Retorna: int: El factorial del número dado. Retorna 0 si el número es 0 o menor.

    Ejemplos:
    >>> factorial(5) 120
    >>> factorial(0) 0
    >>> factorial(3) 6
    """

    if numero <= 0:
        return 0
    resultado = 1
    for num in range(1, numero + 1):
        resultado *= num
    return resultado
