def rekursif(data):
    if len(data) == 1:
        return [data]
    
    nextLayer = []
    for i in range(len(data) - 1):
        nextLayer.append(data[i] + data[i + 1])
    
    hasil = rekursif(nextLayer)
    hasil.append(data)
    return hasil

def main():
    n = int(input())
    data = list(map(int, input().split()))
    data = data[:n]  

    pyramid = rekursif(data)

    for level in pyramid:
        print(" ".join([str(num) for num in level]))

main()