def cariID(data, N):
    kiri, kanan = 0, N

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        
        if tengah < len(data) and data[tengah] == tengah:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    
    return kiri  

def main():
    try:
        N = int(input().strip())  
        data = list(map(int, input().split()))  
        print(cariID(data, N))
    except ValueError:
        print("Input tidak valid")  

main()
