def fibonacci_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    
    fib = [1, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

def generate_id(n):
    if n <= 0:
        return ""
    
    fib = fibonacci_sequence(n)
    result = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_index = 0
    
    for i in range(n):
        if i > 0 and i % 3 == 1:
            result.append(alphabet[alpha_index])
            alpha_index += 1
        else:
            result.append(str(fib[i]))
    
    return " ".join(result)

def main():
    n = int(input())
    print(generate_id(n))

main()