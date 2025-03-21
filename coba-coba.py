import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def countPrimes(seq):
    return sum(1 for x in seq if isPrime(x))

def generatePrimes(n):
    primes, num = [], 2
    while len(primes) < n:
        if isPrime(num):
            primes.append(num)
        num += 1
    return primes

def countMismatches(actual, expected):
    for i, (a, e) in enumerate(zip(actual, expected)):
        if a != e:
            return i
    return -1

def generateSequence(seq, rule):
    if rule == "arithmetic":
        d = seq[1] - seq[0]
        return [seq[0] + d * i for i in range(len(seq))]
    if rule == "geometric":
        r = seq[1] / seq[0]
        return [int(seq[0] * (r ** i)) for i in range(len(seq))]
    if rule == "fibonacci":
        fib = seq[:2]
        for _ in range(2, len(seq)):
            fib.append(fib[-1] + fib[-2])
        return fib
    if rule == "square":
        s = math.isqrt(seq[0])
        return [(s + i) ** 2 for i in range(len(seq))]
    if rule == "prime":
        return generatePrimes(len(seq))
    return []

def detectPattern(seq):
    patterns = ["arithmetic", "geometric", "fibonacci", "square", "prime"]
    for pattern in patterns:
        expected = generateSequence(seq, pattern)
        if seq[:len(expected)] == expected:
            return pattern, expected
    return None, []

def findOutlier(seq):
    if countPrimes(seq) >= len(seq) / 2:
        expected = generatePrimes(len(seq))
        mismatchIdx = countMismatches(seq, expected)
        return mismatchIdx if mismatchIdx != -1 else "Prime Pattern"
    
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    leftPattern, leftExpected = detectPattern(left)
    rightPattern, rightExpected = detectPattern(right)
    
    if leftPattern and (mismatchIdx := countMismatches(left, leftExpected)) != -1:
        return mismatchIdx
    if rightPattern and (mismatchIdx := countMismatches(right, rightExpected)) != -1:
        return mid + mismatchIdx
    return "No Outlier Found"

data = list(map(int, input().split()))
print(findOutlier(data))
