def hidupSantai(n, k, listKuda):
    hitam = [0] * (n + 1)
    putih = [0] * (n + 1)

    for i in range(1, n + 1):
        hitam[i] = hitam[i - 1] + (1 if listKuda[i - 1] == 1 else 0)
        putih[i] = putih[i - 1] + (1 if listKuda[i - 1] == 0 else 0)

    temp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    temp[0][0] = 0  

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for p in range(i):  
                hitamCount = hitam[i] - hitam[p]
                putihCount = putih[i] - putih[p]
                temp[i][j] = min(temp[i][j], temp[p][j - 1] + hitamCount * putihCount)

    return temp[n][k]

def main():
    n, k = map(int, input().split())
    listKuda = [int(input()) for _ in range(n)]

    print(hidupSantai(n, k, listKuda))

main()