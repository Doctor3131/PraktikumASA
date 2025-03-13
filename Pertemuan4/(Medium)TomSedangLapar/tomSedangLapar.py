def pecahData(data, rendah, tinggi):
    basis = data[tinggi]  
    i = rendah  
    for j in range(rendah, tinggi):
        if data[j] > basis:  
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[tinggi] = data[tinggi], data[i]
    return i

def cariTikus(data, rendah, tinggi, k):
    if rendah <= tinggi:
        pi = pecahData(data, rendah, tinggi)
        if pi == k:
            return data[pi]
        elif pi > k:
            return cariTikus(data, rendah, pi - 1, k)
        else:
            return cariTikus(data, pi + 1, tinggi, k)

def cariTerberat(n, k, data):
    return cariTikus(data, 0, n - 1, k - 1)

def main():
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    print(cariTerberat(n, k, data))
