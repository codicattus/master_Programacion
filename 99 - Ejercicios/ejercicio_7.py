bebidas = [
    (10, "Coca-Cola"), 
    (12, "Fanta Naranja"), 
    (25, "Fanta Limón"), 
    (14, "Zumo de Piña"),
    (40, "Batido de chocolate"),
    (30, "Agua con gas"),
    (18, "Tónica"),
# ***********************************************************************************************************  (1, "end"),
    (20, "Vino blanco"),
    (10, "Vino tinto"), 
    (12, "Ginebra"), 
    (5, "Pacharán"), 
    (14, "Ron"),
    (40, "Cerveza"),
    (3, "Martini"),
    (18, "Vodka")
    ]

















def listar_bebidas(x=0):
    for botellas, bebida in bebidas:
        if x < 18 and bebida == "end":
            break
        elif bebida == "end":
            continue
        else:
            print(f"Cantidad: {botellas} de {bebida}.")



























listar_bebidas(5)
