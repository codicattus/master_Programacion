numbers = [1, 5, 2, 4, 6, 7, 8, 9, 11, 25]
num_buscado = 3

for number in numbers:
    if number == num_buscado:
        print(f"Número {num_buscado} encontrado 😀")
        break
else:
    print(f"Número {num_buscado} no encontrado 😥")

# Resultado :
#
# Número 3 no encontrado 😥
#