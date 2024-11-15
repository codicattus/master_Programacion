x = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hh", "ii"], "j"]
print(f"{x[1][1][1] = }")

# Resultado :
# 
# x[1][1][1] = 'ddd'

numbers = [1, 0, 0, 0, 5, 6, 7, 8]
numbers[1:4] = [2, 3, 4]

print(numbers)

# Resultado :
#
# [1, 2, 3, 4, 5, 6, 7, 8]

numbers = [1, 5, 6, 7, 8]
numbers[1:1] = [2, 3, 4]

print(numbers)

# Resultado :
#
# [1, 2, 3, 4, 5, 6, 7, 8]

numbers[1:] = [3, 5, 7, 9]

print(numbers)

# Resultado :
#
# [1, 3, 5, 7, 9]