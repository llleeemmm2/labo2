def get_str(lst):
    return ' '.join(map(str, lst))


size = int(input("Количество строк: "))
triangle = []

for i in range(size):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)

width = len(get_str(triangle[-1]))

for line in triangle:
    print(get_str(line).center(width))