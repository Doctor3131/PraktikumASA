def minBola(H, bola, temp):
    if H == 0:
        return 0  
    if H < 0:
        return float('inf')  
    if H in temp:
        return temp[H]  

    basis = float('inf')
    for b in bola:
        basis = min(basis, 1 + minBola(H - b, bola, temp))

    temp[H] = basis  
    return basis

def main():
    N, H = map(int, input().split())
    bola = list(map(int, input().split()))

    result = minBola(H, bola, {})
    print(result if result != float('inf') else -1)

main()
