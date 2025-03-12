def dungeon(arr):
    if not arr:
        return 0
        
    if all(x < 0 for x in arr):
        return max(arr)
    
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    print(dungeon(arr))

main()