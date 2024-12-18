
def reiniciar_vida():
    global vidas
    vidas = 5

def quitar_vida(cantidad = 1):
    global vidas
    if vidas >= 1:
        vidas -= cantidad

def add_vida(cantidad = 1):
    global vidas
    if vidas <= 4:
        vidas += cantidad

def ver_vidas():
    print(vidas)

# reiniciar_vida()
# print(vidas)
# add_vida()
# print(vidas)
# quitar_vida(2)
# print(vidas)
# add_vida()
# print(vidas)
# ver_vidas()