import json

calorias = {"albaricoque": 48, "fresa": 39, "limón": 44, "mandarina": 50, "manzana": 55, "melón": 21}
print(json.dumps(calorias))
#print(json.dumps(calorias,ensure_ascii=False))
orden_calorico = {3: "albaricoque", 5: "fresa", 4: "limón", 2: "mandarina", 1: "manzana", 6: "melón"}
#print(json.dumps(orden_calorico, ensure_ascii=False))
#print(json.dumps(orden_calorico, ensure_ascii=False, sort_keys=True))
print(json.dumps(orden_calorico, ensure_ascii=False, sort_keys=True, indent= 4))

