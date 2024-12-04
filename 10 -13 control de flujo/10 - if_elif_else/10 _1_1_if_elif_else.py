x = 10
if x > 0:
    print("x es positivo")

print("Esto se mostrará tanto si el número es positivo, negativo o 0")

# Resultado :
#
# x es positivo
# Esto se mostrará tanto si el número es positivo, negativo o 0
#

x = -4
if x > 0:
    print("x es positivo")
else:
    print("Esto solo se mostrará si el número no es positivo")

# Resultado :
#
# Esto solo se mostrará si el número no es positivo
#

x = 0
if x > 0:
    print("x es positivo")
elif x == 0:
    print("Esto solo se mostrará si el número es 0")
else:
    print("Esto solo se mostrará si el número no es positivo o 0")

# Resultado :
#
# Esto solo se mostrará si el número es 0
#

