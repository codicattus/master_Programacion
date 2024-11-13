# Definimos el diccionario
mi_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

hash_dict = {}


for clave in mi_dict.keys():
    valor_hash = hash(clave)
    hash_dict[clave] = valor_hash

for clave, valor_hash in hash_dict.items():
    print(f'Clave: {clave}, Hash: {valor_hash}')
