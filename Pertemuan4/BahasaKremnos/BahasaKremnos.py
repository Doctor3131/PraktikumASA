def isSama(data1, data2):
    if len(data1) != len(data2):
        return False
        
    if data1 == data2:
        return True
        
    if len(data1) % 2 == 1:
        return False
        
    tengah = len(data1) // 2
    a1, a2 = data1[:tengah], data1[tengah:]
    b1, b2 = data2[:tengah], data2[tengah:]
    
    return (isSama(a1, b1) and isSama(a2, b2)) or (isSama(a1, b2) and isSama(a2, b1))

def main():
    data1 = input().strip()
    data2 = input().strip()
    
    if isSama(data1, data2):
        print("YA")
    else:
        print("TIDAK")

main()