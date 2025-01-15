import json

orden_calorico = {3: "albaricoque", 5: "fresa", 4: "limón", 2: "mandarina", 1: "manzana", 6: "melón"}
with open("orden_calorico.json", mode="w", encoding="utf-8") as archivo:
    json.dump(orden_calorico, archivo, ensure_ascii= False)
with open("orden_calorico.json", mode="r", encoding="utf-8") as archivo:
    print(json.load(archivo))

