def minKlu(data, klu):
    def cekBisa(time):
        totalKlu = 0
        for r in data:
            n = 0
            while r * (n + 1) * (n + 1) <= time:
                n += 1
            totalKlu += n
            if totalKlu >= klu:
                return True
        return False

    kiri, kanan = 1, max(data) * klu * klu
    while kiri < kanan:
        tengah = (kiri + kanan) // 2
        if cekBisa(tengah):
            kanan = tengah
        else:
            kiri = tengah + 1

    return kiri

def main():
    data = list(map(int, input().split()))
    klu = int(input().strip())
    print(minKlu(data, klu))

# main()

# def minKlu(data, klu):
#     def cekBisa(time):
#         totalKlu = 0
#         for r in data:
#             kiri, kanan = 1, klu  
#             while kiri < kanan:
#                 tengah = (kiri + kanan) // 2
#                 if r * tengah * tengah <= time:
#                     kiri = tengah + 1
#                 else:
#                     kanan = tengah
#             totalKlu += (kiri - 1)  
#             if totalKlu >= klu:
#                 return True
#         return False

#     kiri, kanan = 1, max(data) * klu * klu
#     while kiri < kanan:
#         tengah = (kiri + kanan) // 2
#         if cekBisa(tengah):
#             kanan = tengah
#         else:
#             kiri = tengah + 1

#     return kiri

# def main():
#     data = list(map(int, input().split()))
#     klu = int(input().strip())
#     print(minKlu(data, klu))

# main()


# def minKlu(data, clue):
#     def cekBisa(time):
#         totalKlu = 0
#         for r in data:
#             kiri, kanan = 1, clue  
#             while kiri < kanan:
#                 tengah = (kiri + kanan + 1) // 2
#                 if r * tengah * tengah <= time:
#                     kiri = tengah
#                 else:
#                     kanan = tengah - 1
#             totalKlu += kiri
#             if totalKlu >= clue:
#                 return True
#         return False

#     kiri, kanan = 1, max(data) * clue * clue
#     while kiri < kanan:
#         tengah = (kiri + kanan) // 2
#         if cekBisa(tengah):
#             kanan = tengah
#         else:
#             kiri = tengah + 1

#     return kiri

# def main():
#     data = list(map(int, input().split()))
#     clue = int(input().strip())
#     print(minKlu(data, clue))

# main()
