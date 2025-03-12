def Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def Factorial(n):
    if n <= 1:
        return 1
    
    temp = 1
    for i in range(2, n+1):
        temp *= i
    
    return temp

def Main():
    n = int(input())
    data = list(map(int, input().split()))
    data = data[:n]  
    switch = int(input())

    temp = 0
    if switch == 1:
        for angka in data:
            temp += Fibonacci(angka)
    elif switch == 2:
        for angka in data:
            temp += Factorial(angka)

    print(temp)

    
Main()