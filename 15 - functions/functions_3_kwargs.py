# def comprobar_tipo_argumentos(*args, otro_valor, **kwargs):
#     print(f"Los args recibidos {args=}, corresponden al tipo {type(args)}")
#     print(f"Los keyword_args recibidos {kwargs=}, corresponden al tipo {type(kwargs)}")
#     print(
#         f"El argumento recibidos {otro_valor=}, corresponden al tipo {type(otro_valor)}"
#     )


# comprobar_tipo_argumentos(5, 6, "Hola", a=1, b=2, c=3, otro_valor=4.5)

# print()
# print(f"*" * 30)
# print(f"*" * 30)
# print()


args = (5, 6, "Hola", 4.5)

kwargs = {"a": 1, "b": 2, "c": 3}


def volver_a_comprobar_tipo_argumentos(*args, **kwargs):
    print(
        f"Los args recibidos por segunda vez {args=}, corresponden al tipo {type(args)}"
    )
    print(
        f"Los keyword_args recibidos por segunda vez {kwargs=}, corresponden al tipo {type(kwargs)}"
    )


# volver_a_comprobar_tipo_argumentos(args, kwargs)


# print()
# print(f"#" * 30)
# print(f"#" * 30)
# print()
volver_a_comprobar_tipo_argumentos(*args, **kwargs)
