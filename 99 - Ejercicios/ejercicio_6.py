
frutas = [
    (10, "manzanas"), 
    (12, "peras"), 
    (3, "sandías"), 
    (14, "naranjas"), 
    (18, "melocotones")
    ]

# Ejercicio:
# Realizar un script que recorra el listado de frutas indicando su peso.
# En el caso que la fruta corresponda con "sandías" o "melones" se debe indicar las unidades en lugar del peso.

# Resultado:
#
# Cantidad: 10kg. de manzanas.
# Cantidad: 12kg. de peras.
# Cantidad: 3kg. de sandías.
# Cantidad: 14kg. de naranjas.
# Cantidad: 18kg. de melocotones.





































# Solución:

for kilos, fruta in frutas:
    if fruta == "sandías" or fruta == "melones":
        print(f"Cantidad: {kilos} {fruta}.")
    else:
        print(f"Cantidad: {kilos}kg. de {fruta}.")