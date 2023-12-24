def point(x, y):
    return x, y


def line_equation_of(p1, M):
    def calculate_c():
        x1, y1 = p1
        c = y1 - M * x1
        return c

    C = calculate_c()
    return f"y = {M:.2f}x + {C:.2f}"


# Menghitung persamaan garis yang melalui titik (4,-2) dan memiliki gradien 2
print("Persamaan garis yang melalui titik (4,-2) dan bergradien 2:")
print(line_equation_of(point(4, -2), -2))
