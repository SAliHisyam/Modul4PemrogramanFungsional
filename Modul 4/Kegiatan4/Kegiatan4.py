import math

# Fungsi untuk menghitung translasi


def translasi(x, y, tx, ty):
    def calculate_translasi():
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return calculate_translasi()

# Fungsi untuk menghitung dilatasi


def dilatasi(x, y, sx, sy):
    def calculate_dilatasi():
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return calculate_dilatasi()

# Fungsi untuk menghitung rotasi


def rotasi(x, y, sudut):
    def calculate_rotasi():
        radians = math.radians(sudut)
        new_x = x * math.cos(radians) - y * math.sin(radians)
        new_y = x * math.sin(radians) + y * math.cos(radians)
        return new_x, new_y
    return calculate_rotasi()


# Koordinat titik P
x_p = 3
y_p = 5

# Translasi dengan tx = 2 dan ty = -1
tx = 2
ty = -1
result_translasi = translasi(x_p, y_p, tx, ty)
print(f"Koordinat setelah translasi: {result_translasi}")

# Dilatasi dengan sx = 2 dan sy = -1
sx = 2
sy = -1
result_dilatasi = dilatasi(x_p, y_p, sx, sy)
print(f"Koordinat setelah dilatasi: {result_dilatasi}")

# Rotasi dengan sudut = 30 derajat
sudut_rotasi = 30
result_rotasi = rotasi(x_p, y_p, sudut_rotasi)
print(f"Koordinat setelah rotasi: {result_rotasi}")
