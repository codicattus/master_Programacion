# -------------- TIPADO FUERTE -------------- #

num1 = "5"
num2 = 5

print(num1 + num2)

# Resultado:
# TypeError: can only concatenate str (not "int") to str

# ------------------------------------------- #

# ------------- TIPADO dinámico ------------- #

item = "Miguel"
print (type(item))

#Resultado:
# <class 'str'>

item = 5
print (type(item))

#Resultado:
# <class 'int'>

item = 5.34
print (type(item))

#Resultado:
# <class 'float'>

item = ["Miguel", 5, 5.34]
print (type(item))

#Resultado:
# <class 'list'>

item = False
print (type(item))

#Resultado:
# <class 'bool'>

# ------------------------------------------- #