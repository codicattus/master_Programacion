# Listas y Tuplas
# Strings: Aunque MyPy puede tener problemas, en tiempo de ejecución funciona.
# Permite extraer elementos y agrupar el resto.

ciudades = "Madrid", "París", "Roma"
cap_SP, cap_FR, cap_IT = ciudades

print(cap_SP)
print(cap_FR)
print(cap_IT)

# Resultado :
#
# Madrid
# París
# Roma
#

palabra = "Hola"

letra1, letra2, *resto = palabra
print(letra1)
print(letra2)
print(resto)

letras1, letras2 = palabra[:2], palabra[2:]
print(letras1)
print(letras2)


