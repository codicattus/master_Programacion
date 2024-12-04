
# ********    Ejercicio    ************ #
# ||||||||||||||||||||||||||||||||||||| #
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv #
# ************************************* #

# Necesito saber cuantas veces sale cada vocal en la palabra de la variable texto
# con el siguiente formato de salida:
#
# La letra u sale un número impar de veces:   1
# La letra e sale un número par de veces:     2
# La letra a sale un número impar de veces:   3
# La letra i sale un número par de veces:     6
# La letra o sale un número impar de veces:   3



texto = "Supercalifragilisticoespialidoso"




















# Pistas
# archivos \strings\methods_1.py, \dict\dict_2.py, \format\format_fstring2.py





































vocales = [char for char in texto if char in 'aeiou']

count_vocales = { vocal: vocales.count(vocal) for vocal in vocales}
for letra in count_vocales:
    if count_vocales[letra] % 2 == 0:
        print(f"La letra {letra} sale un número par de veces: {count_vocales[letra]:>5}")
    else:
        print(f"La letra {letra} sale un número impar de veces: {count_vocales[letra]:>3}")