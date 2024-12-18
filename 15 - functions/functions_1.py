def function_pass():
    pass


def function_pass2(): ...


def sum_without_parameters():
    """Suma 4 más 4 e imprime el resultado por pantalla"""
    print(4 + 4)


def sum_with_two_parameters(num1, num2):
    """Suma los dos números pasados como argumento e imprime el resultado por pantalla"""
    print(num1 + num2)


def sum_with_two_parameters_and_retorn_result(num1, num2):
    """Suma los dos números pasados como argumento e imprime el resultado por pantalla"""
    return num1 + num2


sum_without_parameters()

# Resultado : 8

sum_with_two_parameters(5, 9)

# Resultado : 14

result = sum_with_two_parameters_and_retorn_result(25, 30)
print(result)

# Resultado : 55


# ***************************************************
# Sugerencias de tipo
# Extensión MyPy

# def type_hinting(num1: int, num2: int) -> int:
#    print(num1 + num2)
# ****************************************************

# print(type_hinting("paloma", 5))
