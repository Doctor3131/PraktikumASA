def rekursif(matriks, n, row=1):
    if n == 1 or row >= n:
        return matriks
    
    for col in range(n):
        matriks[row][col] = matriks[row][col] - matriks[row-1][col]
    
    return rekursif(matriks, n, row+1)

def buatNol(matriks, n):
    for i in range(n):
        for j in range(i):
            matriks[i][j] = 0
    return matriks

def main():
    n = int(input())
    
    matriks = []
    for i in range(n):
        row = list(map(int, input().split()))
        matriks.append(row[:n])  

    hasil1 = rekursif(matriks, n)

    hasil2 = buatNol(hasil1, n)

    for row in hasil2:
        print(" ".join([str(angka) for angka in row]))

main()