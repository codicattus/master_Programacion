numbers = [1, 6, 3, 6, 8, 26, 45, 3, 6, 25, 12, 1]
cities = ["Barcelona", "París", "Roma", "Londres", "Berlín"]

print(numbers.count(6))
print(cities.count("Barcelona"))
print(cities.count("arc"))

# Resultado :
#
# 6
# 1
# 0
#

result = list(cities[0])
print(result.count("a"))

# Resultado :
#
# 2
#