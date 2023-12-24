import math

# Decorator untuk transformasi gabungan


def combined_transform(func):
    def wrapper(point, *args):
        for transformation in args:
            point = transformation(point)
        return point
    return wrapper


def line_equation(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept


def translate(point, tx, ty):
    x, y = point
    return x + tx, y + ty


def rotate(point, angle):
    x, y = point
    radians = math.radians(angle)
    return x * math.cos(radians) - y * math.sin(radians), x * math.sin(radians) + y * math.cos(radians)


def scale(point, sx, sy):
    x, y = point
    return x * sx, y * sy

# ecorator


@combined_transform
def combined_transformation(point):
    return point


# Input titik A dan B dari pengguna
point_A = tuple(map(float, input(
    "Masukkan koordinat titik A (pisahkan dengan koma, contoh: 3,4): ").split(',')))
point_B = tuple(map(float, input(
    "Masukkan koordinat titik B (pisahkan dengan koma, contoh: 5,6): ").split(',')))

# Menghitung persamaan garis awal
slope, intercept = line_equation(point_A, point_B)
print("Persamaan Garis yang melalui titik A dan B:")
print(f"y = {slope:.2f}x + {intercept:.2f}")

# Transformasi
tx, ty = 2, -3  # Translasi
angle = 60      # Rotasi
sx, sy = 1.5, 2  # Skala

# Melakukan transformasi gabungan
transformed_point_A = combined_transformation(point_A, lambda p: translate(
    p, tx, ty), lambda p: rotate(p, angle), lambda p: scale(p, sx, sy))
transformed_point_B = combined_transformation(point_B, lambda p: translate(
    p, tx, ty), lambda p: rotate(p, angle), lambda p: scale(p, sx, sy))

# Menghitung persamaan garis setelah transformasi
new_slope, new_intercept = line_equation(
    transformed_point_A, transformed_point_B)
print("\nPersamaan garis baru setelah transformasi:")
print(f"y = {new_slope:.2f}x + {new_intercept:.2f}")
