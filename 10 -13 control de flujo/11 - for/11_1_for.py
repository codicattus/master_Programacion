number_list = [1, 2, 3, 4, 17, 21, 33, 45]
for number in number_list:
    print(number)

# Resultado:
#
# 1
# 2
# 3
# 4
# 17
# 21
# 33
# 45

for number in number_list:
    if number % 2 == 0:
        print(f"El número {number} es par")

# Resultado :
#
# El número 2 es par
# El número 4 es par
# 

for char in "Hello":
    print(char)

# Resultado:
#
# H
# e
# l
# l
# o
#

frutas = [(10, "manzanas"), (12, "peras"), (3, "sandías"), (14, "naranjas")]

for kilos, fruta in frutas:
    if fruta == "sandías":
        print(f"Cantidad: {kilos} {fruta}.")
    else:
        print(f"Cantidad: {kilos}kg. de {fruta}.")

# Resultado:
#
# Cantidad: 10kg. de manzanas.
# Cantidad: 12kg. de peras.
# Cantidad: 3kg. de sandías.
# Cantidad: 14kg. de naranjas.