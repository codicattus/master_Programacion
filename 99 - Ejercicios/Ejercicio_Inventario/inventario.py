# from pathlib import Path
import json

ruta_inventario = '../../recursos/archivos/inventario.json'

def leer_inventario():
    """Lee un archivo JSON y lo convierte en un diccionario."""
    with open(ruta_inventario, 'r', encoding='utf-8') as archivo:
        inventario = json.load(archivo)
    return inventario

def guardar_inventario(inventario):
    """Guarda el inventario como un archivo JSON."""
    with open(ruta_inventario, 'w', encoding='utf-8') as archivo:
        json.dump(inventario, archivo, ensure_ascii=False, indent=4)

def verificar_prenda(nombre,inventario):
    for prenda in inventario:
        if prenda['nombre'].lower() == nombre.lower():
            return True
    return False

def listar_inventario():
    """Imprime un diccionario de inventario."""
    inventario = leer_inventario()
    print(f"Contenido del invernario: {inventario}")
    print("Inventario:")
    for prenda in inventario:
        print(f"\nPrenda: {prenda['nombre']}")
        print(f"Precio: {prenda['precio']}€")
        print("Tallas disponibles:")
        for talla, cantidad in prenda['tallas'].items():
            print(f"  {talla}: {cantidad} unidades")

def agregar_prenda(nombre, precio, tallas):
    """Agrega una nueva prenda al inventario."""
    inventario = leer_inventario()
    if not verificar_prenda(nombre,inventario):
        nueva_prenda = {
            "nombre": nombre,
            "precio": precio,
            "tallas": tallas
        }
        inventario.append(nueva_prenda) 
        guardar_inventario(inventario) 
        print(f"Prenda '{nombre}' agregada al inventario.")
    else:
        print(f"La prenda '{nombre}' ya existe en el inventario.")

agregar_prenda("Pantalón Emidio Tucci", 19.99, {"S": 5, "M": 3, "L": 2})
