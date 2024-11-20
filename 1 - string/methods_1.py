name = "miguel"
last_name = "ANDRÉS"
alias = "H\to\tm\te\tr"
invoice_value = 123456.78
film = "Todos Los Hombres Del Presidente"
lorem = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ullamcorper elit quam, vitae egestas sem dignissim quis. Aenean consectetur interdum quam, non varius ex ullamcorper ut. In varius egestas felis, vel pretium felis. Proin gravida nunc ac eleifend lacinia. Ut congue feugiat lacus eu sagittis. Morbi eros odio, gravida in vulputate vel, sollicitudin at massa. Fusce venenatis vehicula ipsum at ultricies. Pellentesque finibus tortor leo, eu blandit felis volutpat vitae."""
# ------------------------------
print(name.capitalize())
# Resultado:
# Miguel
# ------------------------------

# ------------------------------
print(film.casefold())
# Resultado:
# todos los hombres del presidente
# ------------------------------

# ------------------------------
print(name.center(20, "-"))
# Resultado:
# -------miguel-------
# ------------------------------

# ------------------------------
print(lorem.count("ipsum"))
# Resultado:
# 2
# ------------------------------

# ------------------------------
print(lorem.count("ipsum", 13, 131))
# Resultado:
# 0
# ------------------------------

# ------------------------------
print(last_name.encode())
# Resultado:
# b'ANDR\xc3\x89S'
# ------------------------------

# ------------------------------
print(last_name.encode(encoding="ascii", errors="ignore"))
# Resultado:
# b'ANDRS'
# ------------------------------

# ------------------------------
print(lorem.endswith("vitae."))
print(lorem.endswith("vitae"))
# Resultado:
# True
# False
# ------------------------------

# ------------------------------
print(alias)
print(alias.expandtabs(4))
print(alias.expandtabs(16))
# Resultado:
# H       o       m       e       r
# H   o   m   e   r
# H               o               m               e               r
# ------------------------------

# ------------------------------
print(lorem.find("ipsum"))

# Resultado:
# 7
# ------------------------------