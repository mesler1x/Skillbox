import math

len = float(input())
perimeter = len * 4
square = len ** 2
diagonal = len * math.sqrt(2)

perimeter = round(perimeter, 2)
square = round(square, 2)
diagonal = round(diagonal, 2)

print(str(perimeter) + ",", str(square) + ",", str(diagonal))