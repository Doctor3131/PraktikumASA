def jejak1(data, target, kiri, kanan):
    if kiri > kanan:
        return -1
    
    tengah = (kiri + kanan) // 2
    
    if data[tengah] == target and (tengah == 0 or data[tengah-1] < target):
        return tengah + 1  
    
    if data[tengah] >= target:
        return jejak1(data, target, kiri, tengah-1)
    else:
        return jejak1(data, target, tengah+1, kanan)

def jejak2(data, target, kiri, kanan):
    if kiri > kanan:
        return -1
    
    tengah = (kiri + kanan) // 2
    
    if data[tengah] == target and (tengah == len(data)-1 or data[tengah+1] > target):
        return tengah + 1  
    
    if data[tengah] <= target:
        return jejak2(data, target, tengah+1, kanan)
    else:
        return jejak2(data, target, kiri, tengah-1)

def main():
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    
    first = jejak1(data, k, 0, n-1)
    
    if first == -1:
        print("-1 -1")
    else:
        last = jejak2(data, k, 0, n-1)
        print(first, last)

main()