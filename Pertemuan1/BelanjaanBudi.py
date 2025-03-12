def belanjaanBudi():
    
    a = int(input())
    b = int(input())
    arr = []
    d = input().split(" ")
    
    for i in range(b):
        arr.append(int(d[i]))    
    
    e = cari(a,b,arr)

    print(e[0],e[1])

def cari(a, b, arr):
    for i in range(b-1):
        temp = arr[i]
        for j in range(i+1, b):
            if temp + arr[j] == a:
                return i, j

belanjaanBudi()
