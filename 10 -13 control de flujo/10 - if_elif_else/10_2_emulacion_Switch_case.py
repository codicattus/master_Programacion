def switch(case):
    switcher = {
        1: "Caso 1",
        2: "Caso 2",
        3: "Caso 3"
    }
    return switcher.get(case, "Caso por defecto")

print(switch(1))
print(switch(4)) 

# Resultado :
#
# Caso 1
# Caso por defecto
#

def if_switcher(caso):
    if caso == 1:
        return "Caso 1"
    elif caso == 2:
        return "Caso 2"
    elif caso == 3:
        return "Caso 3"
    else:
        return "Caso por defecto"


print(if_switcher(2))

# Resultado :
#
# Caso 2
#