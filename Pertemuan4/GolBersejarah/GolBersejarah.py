def goals(n, kiri=0, kanan=31):
    if kiri == kanan:
        mask = 2**kiri  
        if (n // mask) % 2 == 1:  
            return 1
        else:
            return 0
    
    tengah = (kiri + kanan) // 2
    
    totKiri = goals(n, kiri, tengah)
    totKanan = goals(n, tengah + 1, kanan)
    
    return totKiri + totKanan


n = int(input().strip())
print(goals(n))
