def main():
    gas = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    if sum(gas) < sum(cost):
        return -1
    
    start,tank = 0,0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    
    return start

print(main())