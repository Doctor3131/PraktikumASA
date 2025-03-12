def main():
    data = input().split()
    dataNew = [int(angka) for angka in data]

    if len(dataNew) % 2 == 0:
        return sum(dataNew)
    else:
        temp = len(dataNew) // 2
        valueTemp = dataNew.pop(temp)
        return valueTemp * sum(dataNew)
    
print(main())

"dengan input '1 2 -1 3 4'"


        