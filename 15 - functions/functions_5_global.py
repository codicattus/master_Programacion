def sumar_nums(*args):
    resultado = 0
    for numero in args:
        resultado = resultado + numero
    return resultado

resultado = sumar_nums(12, 13)
resultado *= 4
print(resultado)

