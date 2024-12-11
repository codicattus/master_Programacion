def if_switcher(tecla):
    if tecla == 1:
        return "tecla 1"
    elif tecla == 2:
        return "tecla 2"
    elif tecla == 3:
        return "tecla 3"
    elif tecla == 4:
        return "tecla 4"
    elif tecla == 5:
        return "tecla 5"
    elif tecla == 6:
        return "tecla 6"
    elif tecla == 7:
        return "tecla 7"
    elif tecla == 8:
        return "tecla 8"
    elif tecla == 9:
        return "tecla 9"
    elif tecla == 0:
        return "tecla 0"
    else:
        return "tecla por defecto"


print(if_switcher(2))

# Resultado :
#
# tecla 2
#


def switch(case):
    switcher = {
        1: "tecla 1",
        2: "tecla 2",
        3: "tecla 3",
        4: "tecla 4",
        5: "tecla 5",
        6: "tecla 6",
        7: "tecla 7",
        8: "tecla 8",
        9: "tecla 9",
        0: "tecla 0"
    }
    return switcher.get(case, "tecla por defecto")

print(switch(1))
print(switch("4")) 

# Resultado :
#
# tecla 1
# tecla por defecto
#