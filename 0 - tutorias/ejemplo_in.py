ciudades = ["Barcelona", "Roma", "París", "Londres"]
letras = ["a", "b", ["cc", "dd"], "e", "f"]

print("********_________************")

for ciudad in ciudades:
    print(ciudad)

# Resultado: 
#
# Barcelona
# Roma
# París
# Londres

for letra in letras:
    print(letra)

# Resultado: 
#
# a
# b
# ['cc', 'dd']
# e
# f

print(len(letras))

# Resultado: 
#
# 5

for i in range(len(ciudades)):
    print(ciudades[i])

# Resultado: 
#
# Barcelona
# Roma
# París
# Londres

for i in range(len(letras)):
    print(letras[i])

# Resultado: 
#
# a
# b
# ['cc', 'dd']
# e
# f