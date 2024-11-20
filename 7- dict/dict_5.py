ciudades = {
    1 : "Barcelona",
    2 : "Madrid"
}

print(ciudades)

states_US = [
    (100, "Arkansas"),
    (101, "Wyoming"), 
    (102, "Oklahoma")
]

ciudades.update(states_US)
print(ciudades)


states_US = [
    (102, "Texas"),
    (103, "Utah"), 
    (104, "Oklahoma")
]

ciudades.update(states_US)
print(ciudades)

# Resultado :
#
# {1: 'Barcelona', 2: 'Madrid'}
# {1: 'Barcelona', 2: 'Madrid', 100: 'Arkansas', 101: 'Wyoming', 102: 'Oklahoma'}
# {1: 'Barcelona', 2: 'Madrid', 100: 'Arkansas', 101: 'Wyoming', 102: 'Texas', 103: 'Utah', 104: 'Oklahoma'}
