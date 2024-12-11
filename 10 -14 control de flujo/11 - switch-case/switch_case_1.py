def switch(tecla):
    match tecla:
        case 1: 
            return "tecla 1 pulsada"
        case 2: 
            return "tecla 2 pulsada"
        case 3: 
            return "tecla 3 pulsada"
        case 4: 
            return "tecla 4 pulsada"
        case 5: 
            return "tecla 5 pulsada"
        case 6: 
            return "tecla 6 pulsada"
        case 7: 
            return "tecla 7 pulsada"
        case 8: 
            return "tecla 8 pulsada"
        case 9: 
            return "tecla 9 pulsada"
        case 0: 
            return "tecla 0 pulsada"
        case _:
            return "no has pulsado un número"
        
print(switch(5))
print(switch("hola"))
    
# Resultado:
#
# tecla 5
# no has introducido un número