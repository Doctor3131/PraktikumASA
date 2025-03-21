def posisi1(data, target):
    kiri, kanan = 0, len(data) - 1
    pertama = -1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            pertama = tengah
            kanan = tengah - 1  
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return pertama

def posisi2(data, target):
    kiri, kanan = 0, len(data) - 1
    akhir = -1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            akhir = tengah
            kiri = tengah + 1  
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return akhir


def main():
    data = list(map(int, input().split()))
    target = int(input())

    pertama = posisi1(data, target)
    akhir = posisi2(data, target)
    print([pertama, akhir])

main()