def cek(data):
    setHuruf = set(data)
    for huruf in setHuruf:
        if huruf.islower() and huruf.upper() not in setHuruf:
            return False
        if huruf.isupper() and huruf.lower() not in setHuruf:
            return False
    return True

def substringBaik(s):
    if len(s) < 2:
        return ""

    terpanjang = 0
    result = ""
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if cek(substring) and len(substring) > terpanjang:
                terpanjang = len(substring)
                result = substring
    
    return result

def main():
    s = input().strip()
    print(substringBaik(s))

main()