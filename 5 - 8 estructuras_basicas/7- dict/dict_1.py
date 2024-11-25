ciudades = {
    "Barcelona" : 1702814,
    "París" : 2206488,
    "Roma" : 2837332,
    "Londres": 8982000,
    "Berlín": 3645000,
    "Sídney": 5312000,
    "Nueva York": 8804000
}

print(type(ciudades))
print(ciudades)

# Resultado :
#
# <class 'dict'>
# {'Barcelona': 1702814, 'París': 2206488, 'Roma': 2837332, 'Londres': 8982000, 'Berlín': 3645000, 'Sídney': 5312000, 'Nueva York': 8804000}

print(f"Berlín tiene {ciudades["Berlín"]} habitantes.")

# Resultado :
#
# Berlín tiene 3645000 habitantes.

print(f"Barcelona: {ciudades.get("Barcelona", "Lo siento no hemos encontrado esta ciudad")}")
print(f"Madagascar: {ciudades.get("Madagascar", "Lo siento no hemos encontrado esta ciudad")}")

# Resultado :
#
# Barcelona: 1702814
# Madagascar: Lo siento no hemos encontrado esta ciudad