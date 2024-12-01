import math

# Deklarasi Fungsi Modul
def  l_persegi(sisi):
    hasil = sisi * sisi 
    print(f'Hasil Perhitungan Luas Persegi {sisi} * {sisi}  = {hasil}')

def l_persegi_panjang(p, l):
    hasil = p * l
    print(f'Hasil Perhitungan Luas Persegi Panjang {p} * {l}  = {hasil}')

def l_segitiga(a, t):
    hasil = 1/2 * a * t
    print(f'Hasil Perhitungan Luas Segitiga {1/2} * {a} * {t}  = {hasil}')

def l_lingkaran(jari):
    hasil = 22/7 * jari * jari
    print(f'Hasil Perhitungan Luas Lingkaran {22/7} * {jari} * {jari}  = {hasil}')

def l_jajargenjang(a, t):
    hasil = a * t
    print(f'Hasil Perhitungan Luas Jajar Genjang {a} * {t}  = {hasil}')