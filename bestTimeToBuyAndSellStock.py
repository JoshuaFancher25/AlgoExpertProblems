# best time to buy and sell stock

def buySell(prices):
    maxpointer = 0
    maxValue = 0
    minPointer = 9999999
    minValue = 9999999
    for i, val in enumerate(prices):
        if val < minValue:
            minValue = val
            minPointer = i
    for j in range(minPointer + 1, len(prices)):
        if prices[j] >= maxValue:
            maxValue = prices[j]
            maxpointer = j
    return maxValue - minValue

array = [2,4,1]

print(buySell(array))