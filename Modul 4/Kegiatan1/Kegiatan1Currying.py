def perkalian(a):
    def dengan(b):
        return a * b
    return dengan


# Menggunakan Currying
hasil_currying = perkalian(5)(10)
print("Hasil perkalian dengan currying:", hasil_currying)
