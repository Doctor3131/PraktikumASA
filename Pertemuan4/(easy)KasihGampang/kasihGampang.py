def binarySearch(data, target):
    if not data:
        return '"Tidak ditemukan"'

    kiri, kanan = 0, len(data) - 1
    isUrutNaik = data[0] < data[-1]

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if data[tengah] == target:
            return tengah
        elif (data[tengah] < target and isUrutNaik) or (data[tengah] > target and not isUrutNaik):
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return '"Tidak ditemukan"'


def main():
    data_input = input().strip()
    if data_input == "[]":
        data = []
    else:
        data = list(map(int, data_input.strip("[]").split(",")))
    
    target = int(input())
    print(binarySearch(data, target))

main()