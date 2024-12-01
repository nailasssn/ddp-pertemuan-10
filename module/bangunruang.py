import math

def  l_kubus(sisi):
    hasil = 6 * sisi * sisi
    print(f'Hasil Perhitungan Luas Permukaan Kubus {6} * {sisi} * {sisi}  = {hasil}')

def l_tabung(jari, t):
    hasil = 22/7 * jari * (jari * t)
    print(f'Hasil Perhitungan Luas Permukaan tabung {22/7} * {jari} * ({jari} * {t})  = {hasil}')

def l_balok(p, l, t):
    hasil = 2 * ((p * l) + (p * t) + (l * t))
    print(f'Hasil Perhitungan Luas Permukaan balok {2} * (({p}*{l}) + ({p}*{t}) + ({l}+{t})) = {hasil}')

def l_prisma(l, k, t):
    hasil = (2 * l) + (k * t)
    print(f'Hasil Perhitungan Luas Permukaan prisma ({2}*{l}) + ({k}*{t}) = {hasil}')
    
def l_limas(la, ls):
    hasil = la + ls
    print(f'Hasil Perhitungan Luas Permukaan limas {la} + {ls} = {hasil}')
