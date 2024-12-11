def switch(tecla):
    match tecla:
        case 1: 
            return "tecla 1"
        case 2: 
            return "tecla 2"
        case 3: 
            return "tecla 3"
        case 4: 
            return "tecla 4"
        case 5: 
            return "tecla 5"
        case 6: 
            return "tecla 6"
        case 7: 
            return "tecla 7"
        case 8: 
            return "tecla 8"
        case 9: 
            return "tecla 9"
        case 0: 
            return "tecla 0"
        case _:
            return "no has introducido un número"
        
print(switch(5))
print(switch("hola"))
    
# Resultado:
#
# tecla 5
# no has introducido un número