# curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan


def kali_dengan(a):
    return perkalian(a)


# Penggunaan HOF
fungsi_kali_dengan_5 = kali_dengan(5)
hasil = fungsi_kali_dengan_5(10)
print("Hasil perkalian dengan HOF:", hasil)
