def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# manual dengan brute force
# def cekSkor(skorPai, skorMinimal):
#     totalSkor = 0
    
#     for skorP in skorPai:
#         tempSkor = 0
#         for skorB in skorMinimal:
#             if skorB <= skorP:
#                 tempSkor += 1
#         totalSkor += tempSkor
    
#     return totalSkor

# karena gabut nunggu test case bikin make binary search
def binSearch(data, target):
    kiri = 0
    kanan = len(data) - 1
    temp = len(data)

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] > target:
            temp = tengah
            kanan = tengah - 1
        else:
            kiri = tengah + 1

    return temp

def main():
    N, K = map(int, input().split())
    skorMinimal = list(map(int, input().split()))
    skorPai = list(map(int, input().split()))

    skorMinimal[:N]
    skorPai[:K]

    sortedSkorMinimal = insertionSort(skorMinimal)
    # print(cekSkor(skorPai,sortedSkorMinimal))

    temp = 0
    for skor in skorPai:
        temp += binSearch(sortedSkorMinimal, skor)
    
    print(temp)

main()