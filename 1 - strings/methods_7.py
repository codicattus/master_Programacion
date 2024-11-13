name ="miguel"
last_name = " Andrés"
password = "PollastreAlast@2022"
film =" Lo Que El Viento Se Llevó"

# El método maketrans() devuelveuna tabla de mapeo 
# que se puede usar conjuntamente con el método translate()
# para reemplazar caracteres específicos.

print(film.translate(str.maketrans("e", "a")))

# Resultado:
# Lo Qua El Vianto Sa Llavó

# Codificación de una contraseña

letter_init ="aeios"
letter_mod = "43105"

change_pass = str.maketrans(letter_init,letter_mod)
print(password.translate(change_pass))

# Resultado:
# P0ll45tr3Al45t@2022