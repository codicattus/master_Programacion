# Crear un set
mi_set = {1, 2, 3, 4, 5}
otro_set = set({4, 5, 6, 7, 7})

print(mi_set)
print(otro_set)


# Agrega un elemento al conjunto. Si el elemento ya está presente, no hace nada.
mi_set.add(6)

# Eliminar un elemento
mi_set.remove(3)

# Devuelve una copia superficial del conjunto.
mi_copia = mi_set.copy() # Salida: {1, 2, 4, 5, 6}

# Elimina todos los elementos del conjunto, dejándolo vacío.
mi_copia.clear()

# Devuelve un nuevo conjunto con los elementos que están en el conjunto original pero no en los otros conjuntos especificados.
diff = mi_set.difference(otro_set) # Salida: {1, 2}

# Actualiza el conjunto original, eliminando los elementos que también están en los otros conjuntos especificados.
mi_set.difference_update(otro_set) # Salida: {1, 2}

# Devuelve un nuevo conjunto que contiene los elementos que están en uno de los conjuntos, pero no en ambos.
diferencia_simetrica = mi_set.symmetric_difference(otro_set) # Salida: {1, 2, 4, 5, 6, 7}


# Actualiza el conjunto original, manteniendo solo los elementos que están en uno de los conjuntos, pero no en ambos. Modifica el conjunto sobre el que se llama.
mi_set.symmetric_difference_update(otro_set) # Salida: {1, 2, 4, 5, 6, 7}


# Devuelve un nuevo conjunto con los elementos comunes a todos los conjuntos especificados.
mi_set.add(4) # Añadido para no dar un conjunto vacío
inter = mi_set.intersection(otro_set) # Salida: {4}

# Actualiza el conjunto original, conservando solo los elementos que son comunes a todos los conjuntos especificados.
mi_set.intersection_update(otro_set) # Salida: {4}

# Devuelve True si dos conjuntos no tienen elementos en común.
tienen_comunes = (mi_set.isdisjoint(otro_set)) # Salida: False

# Devuelve True si todos los elementos del conjunto están en otro conjunto especificado.
set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 3, 4}
es_subconjunto = set_2.issubset(set_1) # Salida: True

# Devuelve True si el conjunto contiene todos los elementos de otro conjunto especificado.
es_superconjunto = set_1.issuperset(set_2) # Salida: True


# Elimina y devuelve un elemento arbitrario del conjunto. Genera un error si el conjunto está vacío. Aunque realmente, a la práctica elimina el primero en la mayoría de ocasiones.
set_3 = {"a", "15", 23, "h"}
elemento = set_3.pop()



# Comprobar si un elemento está en el set
is_in_set = 2 in mi_set
# print(is_in_set)  # Salida: True

# Operaciones de conjuntos

# Unión
union_set = mi_set | otro_set  # {1, 2, 4, 5, 6, 7}

# Intersección
interseccion_set = mi_set & otro_set  # {4, 5, 6}

# Diferencia
diferencia_set = mi_set - otro_set  # {1, 2}
diferencia_set = otro_set - mi_set  # {7}

# Diferencia Simétrica
diferencia_simetrica_set = mi_set ^ otro_set  # {1, 2, 7}


