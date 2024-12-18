def sumar_nums(*args):
    global resultado
    resultado = 0
    for numero in args:
        resultado = resultado + numero


sumar_nums(12, 13)
print(resultado)

