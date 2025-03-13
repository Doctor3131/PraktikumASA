def cariPasanganTerdekat(ketinggian, awal, akhir):
    if akhir - awal == 1:
        return abs(ketinggian[awal] - ketinggian[akhir]), min(awal, akhir) + 1
    
    if akhir - awal == 2:
        selisih1 = abs(ketinggian[awal] - ketinggian[awal+1])
        selisih2 = abs(ketinggian[awal+1] - ketinggian[akhir])
        selisih3 = abs(ketinggian[awal] - ketinggian[akhir])
        
        selisihMinimum = min(selisih1, selisih2, selisih3)
        if selisihMinimum == selisih1:
            return selisihMinimum, min(awal, awal+1) + 1
        elif selisihMinimum == selisih2:
            return selisihMinimum, min(awal+1, akhir) + 1
        else:
            return selisihMinimum, min(awal, akhir) + 1
    
    tengah = (awal + akhir) // 2
    minimumKiri, indeksKiri = cariPasanganTerdekat(ketinggian, awal, tengah)
    minimumKanan, indeksKanan = cariPasanganTerdekat(ketinggian, tengah + 1, akhir)
    
    if minimumKiri < minimumKanan:
        selisihMinimum = minimumKiri
        indeksMinimum = indeksKiri
    elif minimumKanan < minimumKiri:
        selisihMinimum = minimumKanan
        indeksMinimum = indeksKanan
    else:  
        selisihMinimum = minimumKiri  
        indeksMinimum = min(indeksKiri, indeksKanan)
    
    gabungan = [(ketinggian[i], i) for i in range(awal, akhir + 1)]
    gabungan.sort()
    
    for i in range(len(gabungan) - 1):
        selisihSaatIni = abs(gabungan[i][0] - gabungan[i+1][0])
        if selisihSaatIni < selisihMinimum or (selisihSaatIni == selisihMinimum and min(gabungan[i][1], gabungan[i+1][1]) + 1 < indeksMinimum):
            selisihMinimum = selisihSaatIni
            indeksMinimum = min(gabungan[i][1], gabungan[i+1][1]) + 1
    
    return selisihMinimum, indeksMinimum

def cariSelisihMinimum(ketinggian):
    n = len(ketinggian)
    if n < 2:
        return None, None 
    
    return cariPasanganTerdekat(ketinggian, 0, n - 1)

def main():
    n = int(input())
    ketinggian = list(map(int, input().split()))
    
    selisihMinimum, indeksMinimum = cariSelisihMinimum(ketinggian)
    print(f"{selisihMinimum} {indeksMinimum}")

main()