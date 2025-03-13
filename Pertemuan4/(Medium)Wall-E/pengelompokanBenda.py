def grupMinimum(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    grup = []

    for interval in intervals:
        left, right = interval
        ditemukan = False
        for i in range(len(grup)):
            if grup[i] < left:  
                grup[i] = right  
                ditemukan = True
                break

        if not ditemukan:
            grup.append(right)

    return len(grup)

def buatLOL(data):
    data = data.strip()
    if not data or data == "[]":
        return []
    
    data = data[1:-1].strip()
    if not data:
        return []
    
    intervals = []
    pairs = data.split("], [")
    for pair in pairs:
        pair = pair.replace("[", "").replace("]", "")
        left, right = map(int, pair.split(","))
        intervals.append([left, right])
    
    return intervals

def main():
    data = input().strip()
    intervals = buatLOL(data)
    
    if not intervals:
        print(0)
        return
    
    print(grupMinimum(intervals))

main()
