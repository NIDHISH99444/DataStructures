def canCompleteCircuit( gas, cost):
    for i in range(len(gas)):
        if gas[i]>=cost[i]:
            startIndex=i
            break
    n=len(gas)
    originalStartIndex=startIndex
    fuelLeft=0
    while True:
        fuelLeft+=gas[startIndex]-cost[startIndex]
        if fuelLeft<0:
            return -1
        startIndex=(startIndex+1)%n
        if startIndex==originalStartIndex:
            return originalStartIndex
    



gas = [2,3,4]
cost = [3,4,3]
print(canCompleteCircuit( gas, cost))

