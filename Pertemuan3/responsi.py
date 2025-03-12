def main(n):
    hasil = rekursif(n, [], [])
    return hasil

def cekRekursif(data):
    n = len(data)
    if n <= 2:
        return True
    for i in range(1, n-1):
        if not ((data[i] > data[i-1] and data[i] > data[i+1]) or
                (data[i] < data[i-1] and data[i] < data[i+1])):
            return False
    
    return True

def rekursif(n, data, hasil):
    
    if len(data) == n:
        if cekRekursif(data):
            hasil.append(data.copy())
        return hasil
    
    for angka in range(1, n+1):
        if angka not in data:
            data.append(angka)
            rekursif(n, data, hasil)
            data.pop()

    return hasil


def mainFIX(n):
    hasil = []
    rekursif(n, [], hasil)
    return hasil

def cekRekursifFIX(data):
    n = len(data)
    if n <= 2:
        return True
    for i in range(1, n-1):
        if not ((data[i] > data[i-1] and data[i] > data[i+1]) or
                (data[i] < data[i-1] and data[i] < data[i+1])):
            return False
    
    return True

def rekursifFIX(n, data, hasil):
    if len(data) == n:
        if cekRekursif(data):
            hasil.append(data.copy())
        return
    
    for angka in range(1, n+1):
        if angka not in data:
            data.append(angka)
            rekursif(n, data, hasil)  
            data.pop()

n = 6
x = main(n)
y = mainFIX(n)

for i in range(len(x)):

    if x[i] != y[i]:
        print(x[i], "|", y[i])
    else:
        print("sama")