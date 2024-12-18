# raise Exception("Ha ocurrido un error") # Lanza una excepción genérica
# raise ValueError("Valor no válido") # Lanza una excepción específica
# raise ValueError # Lanza una excepción sin argumentos


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("El divisor no puede ser cero")
    return a / b

dividendo, divisor = 10, 0
try:
    resultado = dividir(dividendo, divisor)
except ZeroDivisionError as e:
    resultado = f"Error: {e}"


print(resultado)


# Resultado:
#
# Error: El divisor no puede ser cero

def verificar_positivo(numero):
    if numero < 0:
        raise ValueError("El número debe ser positivo")
    return f"El número {numero} es positivo"

try:
    resultado = verificar_positivo(-5)
    print(resultado)
except ValueError as e:
    print(f"Error: {e}")


# Resultado:
#
# Error: El número debe ser positivo

