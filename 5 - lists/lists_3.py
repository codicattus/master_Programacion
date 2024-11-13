ciudades = ["Barcelona", 1702814, "París", 2206488, "Roma", 2837332, "Londres", 8982000, "Berlín", 3645000, "Sidney", 5312000, "Nueva York", 8804000]

print(f" 1- {ciudades}")
print(f" 2- {ciudades[0]}")
print(f" 3- {ciudades[2:4]}")
print(f" 4- {ciudades[0::2]}")
print(f" 4- {ciudades[0:5:2]}")
print(f" 4- {ciudades[1::2]}")
print(f" 4- {ciudades[1:4:2]}")
print(f" 5- {ciudades[::-1]}")
print(f" 6- {ciudades[4::-1]}")
print(f" 7- {ciudades[8:2:-2]}")


# Resultado :
#
# 1- ['Barcelona', 1702814, 'París', 2206488, 'Roma', 2837332, 'Londres', 8982000, 'Berlín', 3645000, 'Sidney', 5312000, 'Nueva York', 8804000]
# 2- Barcelona
# 3- ['París', 2206488]
# 4- ['Barcelona', 'París', 'Roma', 'Londres', 'Berlín', 'Sidney', 'Nueva York']
# 4- ['Barcelona', 'París', 'Roma']
# 4- [1702814, 2206488, 2837332, 8982000, 3645000, 5312000, 8804000]
# 4- [1702814, 2206488]
# 5- [8804000, 'Nueva York', 5312000, 'Sidney', 3645000, 'Berlín', 8982000, 'Londres', 2837332, 'Roma', 2206488, 'París', 1702814, 'Barcelona']
# 6- ['Roma', 2206488, 'París', 1702814, 'Barcelona']
# 7- ['Berlín', 'Londres', 'Roma']

print(f"\n{"*" * 30}")
print(f"{"*" * 30}\n")

# ----------- Podemos convertir cualquier iterable a una lista con un constructor list() --------------------- #

numbers_list = list(range(10))
print(f"Lista de números del 0 al 9 : \n{numbers_list}")

# Resultado :
# Lista de números del 0 al 9 :
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

letters_list = list("Marianico")
print(f"Letras de Marianico : \n{letters_list}")

# Resultado : 
# Letras de Marianico :
# ['M', 'a', 'r', 'i', 'a', 'n', 'i', 'c', 'o']

# ----------- ************************************************************************* --------------------- #

# ------------- Podemos crear nuevos listas mediante listas por comprensión (list-comprehesion) ------------- #

even_digits = [number for number in range(1, 10) if number % 2 == 0]

print(even_digits)

# Resultado : 
# [2, 4, 6, 8]

even_digits = []
for number in range(1, 10):
    if number % 2 == 0:
        even_digits.append(number)

print(even_digits) 

# Resultado : 
# [2, 4, 6, 8]


# ----------- ************************************************************************* --------------------- #


print(2 in even_digits)
print(5 in even_digits)

# Resultado
# True
# False