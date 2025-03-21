def main():
    data1 = list(map(int, input().split()))
    data2 = list(map(int, input().split()))

    print(cekNaik(data1,data2))

def cekNaik(data1,data2):
    n = len(data1)

    indexData2 = {}
    for i in range(n):
        indexData2[data2[i]] = i

    indexData1diData2 = [indexData2[angka] for angka in data1]

    temp = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if indexData1diData2[i] < indexData1diData2[j] < indexData1diData2[k]:
                    temp += 1

    return temp

main()