def change_pass(password):
    """ Cambia la cadena enviada por otra según los criterios establecidos en la función"""
    letter_init ="aeios"
    letter_mod = "43105"

    change_pass = str.maketrans(letter_init,letter_mod)
    change_pass = password.translate(change_pass)
    return change_pass

print(change_pass("PollastreAlast@2022"))
    
