def main():
    data = input().split(" ")
    data = [int(number) for number in data]

    small1 = smallest(data)

    return small1

def smallest(data: list):
    small = abs(data[1] - data[0])
    for i in range(0, len(data)-1):
        for j in range(i + 1, len(data)):
            if abs(data[i] - data[j]) < small:
                small = abs(data[i] - data[j])
    return small

print(main())
