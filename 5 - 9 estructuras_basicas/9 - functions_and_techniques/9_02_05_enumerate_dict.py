diccionario = {'uno': 1, 'dos': 2, 'tres': 3}

# Sobre las claves

for indice, clave in enumerate(diccionario):
    print(f"Índice: {indice}, Clave: {clave}")

# Sobre los valores

for indice, valor in enumerate(diccionario.values()):
    print(f"Índice: {indice}, Valor: {valor}")

# Sobre los ítems

for indice, (clave, valor) in enumerate(diccionario.items()):
    print(f"Índice: {indice}, Clave: {clave}, Valor: {valor}")

