def cariMayoritas(data, kiri, kanan):
    if kiri == kanan:
        return data[kiri]
    
    tengah = (kiri + kanan) // 2
    
    dataMayoritasKiri = cariMayoritas(data, kiri, tengah)
    dataMayoritasKanan = cariMayoritas(data, tengah + 1, kanan)
    
    if dataMayoritasKiri == dataMayoritasKanan:
        return dataMayoritasKiri
    
    nKiri = sum(1 for i in range(kiri, kanan + 1) if data[i] == dataMayoritasKiri)
    nKanan = sum(1 for i in range(kiri, kanan + 1) if data[i] == dataMayoritasKanan)
    
    if nKiri > (kanan - kiri + 1) // 2:
        return dataMayoritasKiri
    elif nKanan > (kanan - kiri + 1) // 2:
        return dataMayoritasKanan
    else:
        return -1  

def main():
    n = int(input())
    data = list(map(int, input().split()))
    
    mayoritas = cariMayoritas(data, 0, n - 1)
    
    if mayoritas != -1:
        temp = data.count(mayoritas)
        if temp > n // 2:
            print(mayoritas)
        else:
            print(-1)
    else:
        print(-1)

main()