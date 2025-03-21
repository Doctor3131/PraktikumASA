def cekInversi(listNilai, temp=0):
    if len(listNilai) <= 1:
        return temp
    
    for i in range(1, len(listNilai)):
        if listNilai[0] > listNilai[i]:
            temp += 1
        
    return cekInversi(listNilai[1:], temp)


    

def main():
    N = int(input())
    listNilai = list(map(int, input().split()))

    print(cekInversi(listNilai))
main()