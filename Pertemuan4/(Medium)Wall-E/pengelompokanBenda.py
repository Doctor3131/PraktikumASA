# def grupMinimum(intervals):
#     if len(intervals) <= 1:
#         return len(intervals)
    
#     intervals.sort(key=lambda x: x[0])  
    
#     return divideConquer(intervals, 0, len(intervals) - 1)

# def divideConquer(intervals, awal, akhir):
#     if awal == akhir:
#         return 1  
    
#     tengah = (awal + akhir) // 2
    
#     grupKiri = divideConquer(intervals, awal, tengah)
#     grupKanan = divideConquer(intervals, tengah + 1, akhir)
    
#     return merge(intervals, awal, tengah, akhir, grupKiri, grupKanan)

# def merge(intervals, awal, tengah, akhir, grupKiri, grupKanan):
#     merged = []
#     i, j = awal, tengah + 1
    
#     while i <= tengah and j <= akhir:
#         if intervals[i][0] <= intervals[j][0]:
#             merged.append(intervals[i])
#             i += 1
#         else:
#             merged.append(intervals[j])
#             j += 1
    
#     while i <= tengah:
#         merged.append(intervals[i])
#         i += 1
#     while j <= akhir:
#         merged.append(intervals[j])
#         j += 1
    
#     intervals[awal:akhir+1] = merged  
#     active = 0
#     maxGroups = 0
#     events = []
    
#     for left, right in merged:
#         events.append((left, 1))   
#         events.append((right, -1))  

#     events.sort()  

#     for _, event in events:
#         active += event
#         maxGroups = max(maxGroups, active)

#     return max(grupKiri, grupKanan, maxGroups)

# def buatLOL(data):
#     data = data.strip()
#     if not data or data == "[]":
#         return []
    
#     data = data[1:-1].strip()
#     if not data:
#         return []
    
#     intervals = []
#     pairs = data.split("], [")
#     for pair in pairs:
#         pair = pair.replace("[", "").replace("]", "")
#         left, right = map(int, pair.split(","))
#         intervals.append([left, right])
    
#     return intervals

# def main():
#     data = input().strip()
#     intervals = buatLOL(data)
    
#     if not intervals:
#         print(0)
#         return
    
#     print(grupMinimum(intervals))

# main()
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
