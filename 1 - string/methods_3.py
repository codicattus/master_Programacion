name = "Miguel"
last_name= "Andrés"
age = "57"
area = "12²"
username = "Arcangel1347"
password = "@34rT&!55t678ReW"

# 
# Devuelve verdadero si todos los caracteres de la cadena son decimales
#                                                                        
print(age.isdecimal())
print(area.isdecimal())
# Resultado: 
# True
# False
# --------------------------------------------------------------------------------

# 
# Devuelve verdadero si todos los caracteres de la cadena son dígitos
#                                                                        
print(area.isdigit())
print(username.isdigit())
# Resultado: 
# True
# False
# --------------------------------------------------------------------------------

# 
# Devuelve verdadero si todos los caracteres son identificadores válidos
# Un identificador válido sólo puede contener:
# Letras alfanuméricas (a-Z, 0-9) y/o guiones bajos (_).
# No puede comenzar con un número ni contener espacios en blanco.
#                                                                        
print(username.isidentifier())
print(password.isidentifier())
# Resultado: 
# True
# False
# --------------------------------------------------------------------------------