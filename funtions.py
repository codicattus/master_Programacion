def info_user(user_name : str = "usuario", user_email : str = "usario@mail.com") -> None:
    print(f"Hola {user_name}, tu email es: {user_email}")


info_user(user_email= "miguel", user_name="Miguel")

def sumar_edades(*args):
    print(args)

   

print(sumar_edades(5, 4,6, 3, 6))


