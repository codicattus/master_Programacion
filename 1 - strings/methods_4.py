name = "miguel"
last_name= "Andrés"
age = "57"
area = "12²"
username = "Arcangel1347"
password = "@34rT&!55t678ReW"
square = "\u00B2" # símbolo ²
half = "4½"
hello = "Hello \nWorld"
not_space = "                ."
espace = "                    "

# 
# Devuelve verdadero si todos los caracteres de la cadena son minúsculas
#                                                                        
print(name.islower())
print(last_name.islower())
# Resultado: 
# True
# False
# --------------------------------------------------------------------------------

# 
# Devuelve verdadero si todos los caracteres de la cadena son numéricos
#                                                                        
print(age.isnumeric())
print(square.isnumeric())
print(half.isnumeric())
# Resultado: 
# True
# True
# True
# --------------------------------------------------------------------------------

# 
# Devuelve verdadero si todos los caracteres son imprimibles
#                                                                        
print(hello)
print(hello.isprintable())
# Resultado: 
# Hello
# World
# False
# --------------------------------------------------------------------------------

# 
# Devuelve verdadero si todos los caracteres son espacios
#                                                                        
print(not_space.isspace())
print(espace.isspace())
# Resultado: 
# False
# True
# --------------------------------------------------------------------------------