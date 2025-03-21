def hitungJenisUnik(kue, awal, akhir):
    jenis_unik = {}
    jumlah = 0
    for i in range(awal, akhir + 1):
        if kue[i] not in jenis_unik:
            jenis_unik[kue[i]] = 1
            jumlah += 1
    return jumlah

def hitungNilaiSegmen(kue, n):
    nilai = []
    for i in range(n):
        nilai.append([0] * n)
    
    for l in range(n):
        jenis_unik = {}
        for r in range(l, n):
            if kue[r] not in jenis_unik:
                jenis_unik[kue[r]] = 1
            nilai[l][r] = len(jenis_unik)
    
    return nilai

def divideConquer(nilai, awal, akhir, k, temp):
    if k == 1:
        return nilai[awal][akhir]
    
    if akhir - awal + 1 == k:
        return k
    
    key = (awal, akhir, k)
    if key in temp:
        return temp[key]
    
    hasilBest = 0
    
    for i in range(awal, akhir):
        for kiri in range(1, k):
            kanan = k - kiri
            
            if kiri <= i - awal + 1 and kanan <= akhir - i:
                nilaiKiri = divideConquer(nilai, awal, i, kiri, temp)
                nilaiKanan = divideConquer(nilai, i + 1, akhir, kanan, temp)
                hasilBest = max(hasilBest, nilaiKiri + nilaiKanan)
    
    temp[key] = hasilBest
    return hasilBest

def solusiDivideConquer(n, k, kue):
    nilai = hitungNilaiSegmen(kue, n)
    
    temp = {}
    
    return divideConquer(nilai, 0, n - 1, k, temp)

def main():
    line1 = input().strip().split()
    n = int(line1[0])
    k = int(line1[1])
    
    line2 = input().strip().split()
    kue = []
    for x in line2:
        kue.append(int(x))
    
    if len(kue) != n:
        print("Error: Jumlah kue tidak sesuai dengan n")
        return
    
    if k == 1:
        jenis_unik = {}
        for i in range(n):
            if kue[i] not in jenis_unik:
                jenis_unik[kue[i]] = 1
        print(len(jenis_unik))
    else:
        print(solusiDivideConquer(n, k, kue))
    
main()