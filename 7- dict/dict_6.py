user = {
    "name" : " Miguel",
    "age" : 57,
    "zip_code" : "08394"
}

print(user)

# Resultado :
#
# {'name': ' Miguel', 'age': 57, 'zip_code': '08394'}

user["city"] = "Sant Vicenç de Montalt" 

print(user)

# Resultado :
#
# {'name': ' Miguel', 'age': 57, 'zip_code': '08394', 'city': 'Sant Vicenç de Montalt'}


# Nuevo diccionario con el par añadido en la posición deseada
user_nuevo = {}
for clave, valor in user.items():
    user_nuevo[clave] = valor
    if clave == "age":
        user_nuevo["email"] = "codicattus@gmail.com"

print(user_nuevo)

# Resultado :
#
# {'name': ' Miguel', 'age': 57, 'email': 'codicattus@gmail.com', 'zip_code': '08394', 'city': 'Sant Vicenç de Montalt'}


del user_nuevo["age"]
print(user_nuevo)

# Resultado :
#
# {'name': ' Miguel', 'email': 'codicattus@gmail.com', 'zip_code': '08394', 'city': 'Sant Vicenç de Montalt'}
