def sierpinski_triangle(n):
    if n == 0:
        return ["*"]
    else:
        previous = sierpinski_triangle(n - 1)
        space = " " * (2 ** (n - 1))
        result = []
        for line in previous:
            result.append(space + line + space)
        for line in previous:
            result.append(line + " " + line)
        return result


def main():
    depth = int(input("Глубина треугольника:  "))
    triangle = sierpinski_triangle(depth)
    for line in triangle:
        print(line)


main()