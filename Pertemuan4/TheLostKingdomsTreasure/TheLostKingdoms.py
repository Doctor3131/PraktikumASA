def guaTerbesar(data, kiri, kanan):
    if kiri == kanan:
        return data[kiri]
    
    tengah = (kiri + kanan) // 2
    
    maxKiri = guaTerbesar(data, kiri, tengah)
    maxKanan = guaTerbesar(data, tengah + 1, kanan)
    
    return max(maxKiri, maxKanan)


def main():
    n = int(input())
    dataUkuranGua = list(map(int, input().split()))

    print(guaTerbesar(dataUkuranGua, 0, n - 1))

main()