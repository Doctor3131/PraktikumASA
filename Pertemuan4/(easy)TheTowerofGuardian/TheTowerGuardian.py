def isSampeAtas(P, listPenjaga):
    # for penjaga in listPenjaga:
    #     if penjaga > P:
    #         return False
    #     P += penjaga
    # print(f"{P} = {listPenjaga}")

    if len(listPenjaga) == 0:
        return True

    else:
        if P > listPenjaga[0]:
            return isSampeAtas(P + listPenjaga[0], listPenjaga[1:])
        else:
            return False

def main():
    N, P = map(int, input().split())
    listPenjaga = list(map(int, input().split()))

    if isSampeAtas(P, listPenjaga):
        print("YES")
    else:
        print("NO")
    print(isSampeAtas(P, listPenjaga))

main()