def modMergeSort(data):
    if len(data) <= 1:
        return data, 0
    
    tengah = len(data) // 2
    kiri, basisKiri = modMergeSort(data[:tengah])
    kanan, basisKanan = modMergeSort(data[tengah:])
    temp, basisQonquer = qonquer(kiri, kanan)
    
    return temp, basisKiri + basisKanan + basisQonquer

def qonquer(kiri, kanan):
    temp = []
    basis = 0
    i = 0
    j = 0
    
    while i < len(kiri) and j < len(kanan):
        if kiri[i] <= kanan[j]:
            temp.append(kiri[i])
            i += 1
        else:
            temp.append(kanan[j])
            basis += len(kiri) - i
            j += 1
    
    while i < len(kiri):
        temp.append(kiri[i])
        i += 1
        
    while j < len(kanan):
        temp.append(kanan[j])
        j += 1
    
    return temp, basis

def main():
    n = int(input())
    data = list(map(int, input().split()))
    data = data[:n]
    print(modMergeSort(data)[1])
    

main()