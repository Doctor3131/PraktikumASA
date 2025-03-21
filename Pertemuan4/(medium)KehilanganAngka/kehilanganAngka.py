def cariAngka(data, n):
    dataSet = set(data)
    
    def binarySearch(kiri, kanan):
        if kiri > kanan:
            return kiri - 1
        
        if kiri == kanan:
            if kiri in dataSet:
                return kiri - 1
            else:
                return kiri
        
        tengah = (kiri + kanan) // 2
        
        if tengah not in dataSet:
            return binarySearch(tengah + 1, kanan)
        else:
            kanan_result = binarySearch(tengah + 1, kanan)
            if kanan_result > tengah:
                return kanan_result
            return binarySearch(kiri, tengah - 1)
    
    return binarySearch(0, n)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    hasil = cariAngka(data, n)
    print(hasil)

main()