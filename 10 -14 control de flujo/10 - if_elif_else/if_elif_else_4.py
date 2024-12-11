num = 22
grupo_user = "comunidad"
vip = False


condicion = [ num > 18, num < 30, grupo_user == "comunidad", vip == True]

if all(condicion):
    print("Se etán cumpliendo todas las condiciones")

if any(condicion):
    print("Sólo se cumplen una o varias condiciones")