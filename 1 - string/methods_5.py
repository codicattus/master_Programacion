name = "miguel"
last_name= "Andrés"
age = "57"
area = "12²"
film1 = "Lo Que El Viento Se Llevó"
film2 = "Lo Que El Viento SE Llevó"
serie = "FALLOUT"
spaces = "         Hola     "
spaces2 = "-,.wwwsddd          Hola       ---,.....wssssddddd"

# 
# Devuelve verdadero si todas las palabras de la cadena comienzan con una letra mayúscula y el resto de la palabra son minúsculas.
#                                                                        
print(film1.istitle())
print(film2.istitle())
# Resultado: 
# True
# False
# --------------------------------------------------------------------------------

# 
# Devuelve verdadero si todas los caracteres del texto están en mayúsculas
#                                                                        
print(serie.isupper())
print(film1.isupper())
# Resultado: 
# True
# False
# --------------------------------------------------------------------------------

# 
# Toma todos los elementos de un iterable y los une en una cadena
#                                                                        
print("-".join(name))
print("* *".join(name))
# Resultado: 
# m-i-g-u-e-l
# m* *i* *g* *u* *e* *l
# --------------------------------------------------------------------------------

# 
# Borra todos los caracteres indicados (espacio por defecto) a la izquierda de la cadena.
#                                                                        
print(spaces.lstrip(),"Mundo")
print(spaces2.lstrip("-,.wsd "),"Mundo")
# Resultado: 
# Hola      Mundo 
# Hola       ---,.....wssssddddd Mundo
# --------------------------------------------------------------------------------

# 
# Borra todos los caracteres indicados (espacio por defecto) a la derecha de la cadena.
#                                                                        
print(spaces.rstrip(),"Mundo")
print(spaces2.rstrip("-,.wsd "),"Mundo")
# Resultado: 
# Hola      Mundo 
# Hola       ---,.....wssssddddd Mundo
# --------------------------------------------------------------------------------