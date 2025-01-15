import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect("calorias.db")
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS frutas (
        nombre TEXT PRIMARY KEY,
        calorias INTEGER
    )
''')

# Insertar datos
frutas = [
    ("albaricoque", 72),
    ("mango", 39),
    ("limón", 44),
    ("mandarina", 50),
    ("manzana", 55),
    ("melón", 21)
]

cursor.executemany("INSERT OR REPLACE INTO frutas (nombre, calorias) VALUES (?, ?)", frutas)
conn.commit()

# Añadir otra fruta
cursor.execute("INSERT OR REPLACE INTO frutas (nombre, calorias) VALUES (?, ?)", ("pera", 57))
conn.commit()

# Leer los datos
cursor.execute("SELECT * FROM frutas")
resultado = cursor.fetchall()
for fila in resultado:
    print(fila)


# Añadir fruta

nueva_fruta = ("kiwi", 61)
cursor.execute("INSERT OR REPLACE INTO frutas (nombre, calorias) VALUES (?, ?)", nueva_fruta)
conn.commit()

# Buscar fruta
fruta_buscada = "fresa"
cursor.execute("SELECT * FROM frutas WHERE nombre = ?", (fruta_buscada,))
resultado = cursor.fetchone()
if resultado:
    print(f"Fruta: {resultado[0]}, Calorías: {resultado[1]}")
else:
    print(f"{fruta_buscada} no encontrado en la base de datos.")


# Cerrar la conexión
conn.close()



# Por seguridad (Inyección SQL) NO HAGAS ESTO
# nombre = "kiwi"
# calorias = 61
# consulta = f"INSERT INTO frutas (nombre, calorias) VALUES ('{nombre}', {calorias})"
# cursor.execute(consulta)
