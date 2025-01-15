import json

calorias = {"albaricoque": 48, "fresa": 39, "limón": 44, "mandarina": 50, "manzana": 55, "melón": 21}
with open("calorias.json", mode="w", encoding="utf-8") as archivo:
#with open("./16 - trabajando con archivos/json/calorias.json", mode="w", encoding="utf-8") as archivo:
    json.dump(calorias, archivo, ensure_ascii= False)