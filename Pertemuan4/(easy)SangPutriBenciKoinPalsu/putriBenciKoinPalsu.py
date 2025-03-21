def cariKoinPalsu(koin, awal, akhir):
    if awal == akhir:
        return awal  

    n = akhir - awal
    tengah = awal + (n // 2)

    if n % 2 == 0:  
        bagian1 = koin[awal:tengah]  
        bagian2 = koin[tengah:akhir+1]  
    else:  
        bagian1 = koin[awal:tengah]  
        bagian2 = koin[tengah+1:akhir+1]  

    if sum(bagian1) < sum(bagian2):  
        return cariKoinPalsu(koin, awal, tengah-1)  
    elif sum(bagian1) > sum(bagian2):  
        return cariKoinPalsu(koin, tengah, akhir)  
    else:  
        return tengah  

def main():
    N = int(input())  
    data = list(map(int, input().split()))  

    hasil = cariKoinPalsu(data, 0, N - 1)  
    print(hasil + 1)  

main()
