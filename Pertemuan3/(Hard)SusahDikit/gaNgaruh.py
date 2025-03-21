# import math

# def cekPrima(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def nPrima(dataCek):
#     return sum(1 for i in dataCek if cekPrima(i))

# def cekNPrimaBenar(n):
#     dataCek = []
#     temp = 2
#     while len(dataCek) < n:
#         if cekPrima(temp):
#             dataCek.append(temp)
#         temp += 1
#     return dataCek

# def hitungBeda(dataAsli, dataCek):
#     beda = 0
#     indexAwal = None
#     for i, (j, k) in enumerate(zip(dataAsli, dataCek)):
#         if j != k:
#             beda += 1
#             if indexAwal is None:
#                 indexAwal = i
#     return beda, indexAwal

# def arithmetic_expected(dataCek):
#     d = dataCek[1] - dataCek[0]
#     return [dataCek[0] + d * i for i in range(len(dataCek))]

# def arithmetic_expected_cont(dataCek, count):
#     d = dataCek[1] - dataCek[0]
#     start = dataCek[-1]
#     return [start + d * (i+1) for i in range(count)]

# def geometric_expected(dataCek):
#     r = dataCek[1] / dataCek[0]
#     return [int(dataCek[0] * (r ** i)) for i in range(len(dataCek))]

# def geometric_expected_cont(dataCek, count):
#     r = dataCek[1] / dataCek[0]
#     start = dataCek[-1]
#     return [int(start * (r ** (i+1))) for i in range(count)]

# def fibonacci_expected(dataCek):
#     if len(dataCek) < 2:
#         return dataCek[:]
#     exp = dataCek[:2]
#     for i in range(2, len(dataCek)):
#         exp.append(exp[i-1] + exp[i-2])
#     return exp

# def fibonacci_expected_cont(dataCek, count):
#     if len(dataCek) < 2:
#         return []
#     a, b = dataCek[-2], dataCek[-1]
#     res = []
#     for i in range(count):
#         c = a + b
#         res.append(c)
#         a, b = b, c
#     return res

# def square_expected(dataCek):
#     s = math.isqrt(dataCek[0])
#     return [(s + i) ** 2 for i in range(len(dataCek))]

# def square_expected_cont(dataCek, count):
#     s = math.isqrt(dataCek[0])
#     last_root = math.isqrt(dataCek[-1]) if is_perfect_square(dataCek[-1]) else s + len(dataCek) - 1
#     return [(last_root + i + 1) ** 2 for i in range(count)]

# def is_perfect_square(n):
#     r = math.isqrt(n)
#     return r * r == n

# def prime_expected(dataCek):
#     # Selalu hasilkan deret bilangan prima mulai dari 2
#     n = len(dataCek)
#     return cekNPrimaBenar(n)

# def prime_expected_cont(dataCek, count):
#     n = len(dataCek)
#     full = cekNPrimaBenar(n + count)
#     return full[n:]

# # Daftar temp pattern dengan format:
# # (name, expected_func, continuation_func)
# pattern_candidates = [
#     ("square", square_expected, square_expected_cont),
#     ("arithmetic", arithmetic_expected, arithmetic_expected_cont),
#     ("geometric", geometric_expected, geometric_expected_cont),
#     ("fibonacci", fibonacci_expected, fibonacci_expected_cont),
#     ("prime", prime_expected, prime_expected_cont)
# ]

# def detect_pattern_tolerant(dataCek):
#     best = (None, None, None, float('inf'), None)
#     for name, exp_func, cont_func in pattern_candidates:
#         if name == "square" and not is_perfect_square(dataCek[0]):
#             continue
#         if name == "geometric" and dataCek[0] == 0:
#             continue
#         exp_seq = exp_func(dataCek)
#         beda, first_index = hitungBeda(dataCek, exp_seq)
#         if beda < best[3]:
#             best = (name, exp_func, cont_func, beda, first_index)
#     return best

# # --- Main Program ---
# dataCek = list(map(int, input().split()))
# n = len(dataCek)

# # Jika mayoritas elemen full input adalah bilangan prima, gunakan pola prime untuk full input
# if nPrima(dataCek) >= len(dataCek) / 2:
#     expected_full = cekNPrimaBenar(n)
#     beda, first_index = hitungBeda(dataCek, expected_full)
#     if beda > 0:
#         print(first_index)
#     else:
#         print("Full input follows prime pattern.")
#     exit()

# # Pembagian: jika jumlah elemen ganjil, left dapatkan elemen ekstra
# mid = (n + 1) // 2
# left = dataCek[:mid]
# right = dataCek[mid:]

# left_pattern, left_exp_func, left_cont_func, left_mismatch_count, left_first_mismatch = detect_pattern_tolerant(left)
# right_pattern, right_exp_func, right_cont_func, right_mismatch_count, right_first_mismatch = detect_pattern_tolerant(right)

# # Pilih temp side berdasarkan apakah terdapat error (mismatch > 0)
# if left_pattern is not None and left_mismatch_count > 0:
#     candidate_side = "left"
# elif right_pattern is not None and right_mismatch_count > 0:
#     candidate_side = "right"
# else:
#     if left_pattern is None and right_pattern is None:
#         print("No pattern recognized on both sides.")
#         exit()
#     if left_pattern is None:
#         candidate_side = "right"
#     elif right_pattern is None:
#         candidate_side = "left"
#     else:
#         candidate_side = "left" if len(left) >= len(right) else "right"

# if candidate_side == "left":
#     candidate_list = left
#     candidate_offset = 0
#     pattern_name = left_pattern
#     cont_func = left_cont_func
#     mismatch_count = left_mismatch_count
#     indexAwal = left_first_mismatch
#     other_side = right
#     other_offset = mid
# else:
#     candidate_list = right
#     candidate_offset = mid
#     pattern_name = right_pattern
#     cont_func = right_cont_func
#     mismatch_count = right_mismatch_count
#     indexAwal = right_first_mismatch
#     other_side = left
#     other_offset = 0

# if mismatch_count > 0:
#     print(candidate_offset + indexAwal)
# else:
#     expected_other = cont_func(candidate_list, len(other_side))
#     beda, first_mismatch = hitungBeda(other_side, expected_other)
#     if beda > 0:
#         print(other_offset + first_mismatch)
#     else:
#         print("error")

import math

def cekPrima(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def hitungJumlahPrima(dataCek):
    return sum(1 for i in dataCek if cekPrima(i))

def daftarPrima(n):
    dataCek = []
    temp = 2
    while len(dataCek) < n:
        if cekPrima(temp):
            dataCek.append(temp)
        temp += 1
    return dataCek

def hitungPerbedaan(dataAsli, dataCek):
    beda = 0
    indeksAwal = None
    for i, (j, k) in enumerate(zip(dataAsli, dataCek)):
        if j != k:
            beda += 1
            if indeksAwal is None:
                indeksAwal = i
    return beda, indeksAwal

def deretAritmetika(dataCek):
    beda = dataCek[1] - dataCek[0]
    return [dataCek[0] + beda * i for i in range(len(dataCek))]

def lanjutkanDeretAritmetika(dataCek, jumlah):
    beda = dataCek[1] - dataCek[0]
    awal = dataCek[-1]
    return [awal + beda * (i+1) for i in range(jumlah)]

def deretGeometri(dataCek):
    rasio = dataCek[1] / dataCek[0]
    return [int(dataCek[0] * (rasio ** i)) for i in range(len(dataCek))]

def lanjutkanDeretGeometri(dataCek, jumlah):
    rasio = dataCek[1] / dataCek[0]
    awal = dataCek[-1]
    return [int(awal * (rasio ** (i+1))) for i in range(jumlah)]

def deretFibonacci(dataCek):
    if len(dataCek) < 2:
        return dataCek[:]
    exp = dataCek[:2]
    for i in range(2, len(dataCek)):
        exp.append(exp[i-1] + exp[i-2])
    return exp

def lanjutkanDeretFibonacci(dataCek, jumlah):
    if len(dataCek) < 2:
        return []
    a, b = dataCek[-2], dataCek[-1]
    hasil = []
    for i in range(jumlah):
        c = a + b
        hasil.append(c)
        a, b = b, c
    return hasil

def deretKuadrat(dataCek):
    s = math.isqrt(dataCek[0])
    return [(s + i) ** 2 for i in range(len(dataCek))]

def lanjutkanDeretKuadrat(dataCek, jumlah):
    s = math.isqrt(dataCek[0])
    akarTerakhir = math.isqrt(dataCek[-1]) if cekKuadratSempurna(dataCek[-1]) else s + len(dataCek) - 1
    return [(akarTerakhir + i + 1) ** 2 for i in range(jumlah)]

def cekKuadratSempurna(n):
    r = math.isqrt(n)
    return r * r == n

def deretPrima(dataCek):
    return daftarPrima(len(dataCek))

def lanjutkanDeretPrima(dataCek, jumlah):
    panjang = len(dataCek)
    penuh = daftarPrima(panjang + jumlah)
    return penuh[panjang:]

polaKandidat = [
    ("kuadrat", deretKuadrat, lanjutkanDeretKuadrat),
    ("aritmetika", deretAritmetika, lanjutkanDeretAritmetika),
    ("geometri", deretGeometri, lanjutkanDeretGeometri),
    ("fibonacci", deretFibonacci, lanjutkanDeretFibonacci),
    ("prima", deretPrima, lanjutkanDeretPrima)
]

def deteksiPolaToleran(dataCek):
    terbaik = (None, None, None, float('inf'), None)
    for nama, fungsiEkspektasi, fungsiLanjutan in polaKandidat:
        if nama == "kuadrat" and not cekKuadratSempurna(dataCek[0]):
            continue
        if nama == "geometri" and dataCek[0] == 0:
            continue
        ekspektasi = fungsiEkspektasi(dataCek)
        beda, indeksAwal = hitungPerbedaan(dataCek, ekspektasi)
        if beda < terbaik[3]:
            terbaik = (nama, fungsiEkspektasi, fungsiLanjutan, beda, indeksAwal)
    return terbaik

def main():
    dataCek = list(map(int, input().split()))
    n = len(dataCek)

    if hitungJumlahPrima(dataCek) >= len(dataCek) / 2:
        ekspektasiPenuh = daftarPrima(n)
        beda, indeksAwal = hitungPerbedaan(dataCek, ekspektasiPenuh)
        print(indeksAwal if beda > 0 else "Deret mengikuti pola prima sepenuhnya.")
        exit()

    mid = (n + 1) // 2
    kiri = dataCek[:mid]
    kanan = dataCek[mid:]

    polaKiri, ekspektasiKiri, lanjutanKiri, bedaKiri, indeksAwalKiri = deteksiPolaToleran(kiri)
    polaKanan, ekspektasiKanan, lanjutanKanan, bedaKanan, indeksAwalKanan = deteksiPolaToleran(kanan)

    if polaKiri is not None and bedaKiri > 0:
        print(indeksAwalKiri)
    elif polaKanan is not None and bedaKanan > 0:
        print(mid + indeksAwalKanan)
    else:
        if polaKiri is None and polaKanan is None:
            print("Tidak ada pola yang dikenali.")
            exit()
        kandidatPola, kandidatData, offset = (polaKiri, kiri, 0) if polaKiri else (polaKanan, kanan, mid)
        fungsiLanjutan = lanjutanKiri if polaKiri else lanjutanKanan
        ekspektasiLawan = fungsiLanjutan(kandidatData, len(kiri if polaKanan else kanan))
        beda, indeksAwal = hitungPerbedaan(kanan if polaKiri else kiri, ekspektasiLawan)
        print(offset + indeksAwal if beda > 0 else "error")

main()