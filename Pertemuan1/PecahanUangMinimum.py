def main():
    x = int(input())
    count = 0
    while x > 0:
        if (x >= 50):
            count += 1
            x -= 50
        elif (x >= 25):
            count += 1
            x -= 25
        elif (x >= 10):
            count += 1
            x -= 10
        elif (x >= 5):
            count += 1
            x -= 5
        else:
            count += 1
            x -= 1
    return count

print(main())