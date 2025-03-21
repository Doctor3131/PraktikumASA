def binarySearch(data: list):
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if (tengah == 0 or data[tengah] > data[tengah - 1]) and \
           (tengah == len(data) - 1 or data[tengah] > data[tengah + 1]):
            return tengah + 1  

        if tengah < len(data) - 1 and data[tengah] < data[tengah + 1]:
            kiri = tengah + 1
        else: 
            kanan = tengah - 1

def main():
    N = int(input()) 
    A = list(map(int, input().split()))  

    print(binarySearch(A))

main()