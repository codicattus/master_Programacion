name ="        miguel         "
last_name = " Andrés"
password = "PollastreAlast@2022"
film =" Lo Que El Viento Se Llevó"
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer placerat bibendum est, pharetra semper risus tincidunt at. Sed auctor, nunc eu interdum cursus, nulla purus imperdiet leo, quis viverra urna arcu quis dolor. Mauris condimentum mauris sed sagittis blandit. Curabitur massa est, iaculis et ultrices a, pulvinar in mauris. Nulla blandit ac leo at maximus. Aenean tristique non lacus at feugiat. Donec varius condimentum enim, eu rhoncus odio molestie ac. Donec aliquam, massa in imperdiet rhoncus, odio neque ultricies ante, et accumsan quam leo sit amet est. Suspendisse condimentum ornare neque eu tristique. Duis porta posuere mi id tincidunt. Morbi in sem ac libero tristique bibendum a quis arcu. Interdum et malesuada fames ac ante ipsum primis in faucibus. In porttitor orci id dapibus placerat. Curabitur elementum mauris eros, in lobortis magna feugiat eu. Aenean id accumsan sem. Donec vel elit mauris.

Aenean et tempor est, eget accumsan eros. Sed a pharetra magna. Mauris a tortor ut massa bibendum lobortis quis eu risus. Nam congue odio tortor, ut dictum quam pharetra eget. Morbi et nulla id magna efficitur bibendum lobortis vitae enim. Sed lacinia eros et ante congue consequat. Nullam non sollicitudin tellus. Praesent fringilla, turpis nec feugiat pharetra, nulla nunc egestas ex, tristique eleifend turpis nunc eget sapien. Donec id vulputate urna, ut porta nunc."""

# El método partition() busca una subcadena específica y divide la cadena en una tupla con las tres subcadenas resultantes.

print(film.partition("El Viento"))

# Resultado:
# (' Lo Que ', 'El Viento', ' Se Llevó')

# ---------------------------------------------------------------------------------------------------------------------------- #

# El método replace() cambiauna parte de la cadena por otra especifcada.

print(film.replace("El Viento", "El Huracán"))

# Resultado:
# Lo Que El Huracán Se Llevó

# ---------------------------------------------------------------------------------------------------------------------------- #

# El método rfind() la última ocurrencia del valor especificado.

print(lorem.rfind("Donec"))

# Resultado:
# 1357

# ---------------------------------------------------------------------------------------------------------------------------- #

# El método split() devuelve una lista con cada una de las palabras de la cadena.

print(film.split())

# Resultado:
# ['Lo', 'Que', 'El', 'Viento', 'Se', 'Llevó']


# ---------------------------------------------------------------------------------------------------------------------------- #

# El método strip() elimina los espacios (o los caracteres indicados) a la izquierda y derecha de la cadena.

print(name.strip(), last_name.lower())

# Resultado:
# miguel  andrés

# ---------------------------------------------------------------------------------------------------------------------------- #

# El método swapcase() intercambia mayúsculas por minúsculas y viceversa.

print(film.swapcase())

# Resultado:
#  lO qUE eL vIENTO sE lLEVÓ
