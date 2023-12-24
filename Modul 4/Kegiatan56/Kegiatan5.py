def point(x, y):
    return x, y


def line_equation_of(p1, p2):
    # Gradien (m) adalah perubahan y dibagi perubahan x antara dua titik
    M = (p2[1] - p1[1]) / (p2[0] - p1[0])

    # Gunakan salah satu titik (misalnya p1) dan gradien (m) untuk mencari konstanta (c)
    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"


# Menghitung persamaan garis yang melalui titik A(1, 3) dan B(5, 9)
print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 4), point(2, 2)))
