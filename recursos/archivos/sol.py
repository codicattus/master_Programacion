# Datos iniciales

"""
Gestor de Inventario de una Tienda de Ropa

Crear un programa que gestione el inventario de una tienda de ropa donde:

1. Tendrás un inventario inicial con esta estructura:
   - Cada prenda será un diccionario con: nombre, precio, tallas disponibles y cantidad por talla
   - El inventario será una lista de estas prendas

2. El programa deberá:
   a) Mostrar todo el inventario de forma ordenada
   b) Buscar prendas por nombre (sin importar mayúsculas/minúsculas)
   c) Mostrar todas las prendas de un rango de precio específico
   d) Actualizar la cantidad de una prenda en una talla específica
   e) Mostrar las prendas con poco stock (menos de 3 unidades en alguna talla)

Datos de ejemplo para iniciar el inventario:
inventario = [
    {
        "nombre": "Camiseta Básica",
        "precio": 15.99,
        "tallas": {"S": 5, "M": 4, "L": 7}
    },
    {
        "nombre": "Pantalón Vaquero",
        "precio": 49.99,
        "tallas": {"M": 6, "L": 8, "XL": 2}
    },
    {
        "nombre": "Sudadera",
        "precio": 29.99,
        "tallas": {"S": 2, "M": 8, "L": 3}
    }
]
"""





































def mostrar_inventario():
    for prenda in inventario:
        print(f"\nPrenda: {prenda['nombre']}")
        print(f"Precio: {prenda['precio']}€")
        print("Tallas disponibles:")
        for talla, cantidad in prenda['tallas'].items():
            print(f"  {talla}: {cantidad} unidades")

def buscar_prenda(nombre):
    for prenda in inventario:
        if nombre.lower() in prenda['nombre'].lower():
            print(f"\nEncontrada: {prenda['nombre']}")
            print(f"Precio: {prenda['precio']}€")
            print("Tallas:", prenda['tallas'])

def filtrar_por_precio(min_precio, max_precio):
    print(f"\nPrendas con precio entre {min_precio}€ y {max_precio}€:")
    print("*" * 35)
    for prenda in inventario:
        if min_precio <= prenda['precio'] <= max_precio:
            print(f"{prenda['nombre']} - {prenda['precio']}€")

def actualizar_cantidad(nombre, talla, nueva_cantidad):
    for prenda in inventario:
        if prenda['nombre'].lower() == nombre.lower():
            if talla in prenda['tallas']:
                prenda['tallas'][talla] = nueva_cantidad
                print(f"Cantidad actualizada para {prenda['nombre']}")
                return
    print("Prenda o talla no encontrada")

def mostrar_poco_stock():
    for prenda in inventario:
        tallas_poco_stock = [
            talla for talla, cantidad in prenda['tallas'].items() 
            if cantidad < 3
        ]
        if tallas_poco_stock:
            print(f"\n{prenda['nombre']} tiene poco stock en tallas:", 
                  ", ".join(tallas_poco_stock))

inventario = [
    {
        "nombre": "Camiseta Básica",
        "precio": 15.99,
        "tallas": {"S": 5, "M": 4, "L": 7}
    },
    {
        "nombre": "Pantalón Vaquero",
        "precio": 49.99,
        "tallas": {"M": 6, "L": 8, "XL": 2}
    },
    {
        "nombre": "Sudadera",
        "precio": 29.99,
        "tallas": {"S": 2, "M": 8, "L": 3}
    }
]

mostrar_inventario()
buscar_prenda("Pantalón")
filtrar_por_precio(20, 50)