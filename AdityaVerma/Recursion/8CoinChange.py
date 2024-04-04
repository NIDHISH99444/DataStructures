def coinChange(coins, index, amount, memo):
    if amount == 0:
        return 0

    if index == len(coins) or amount < 0:
        return float('inf')

    if memo[index][amount] != -1:
        return memo[index][amount]

    include = 1 + coinChange(coins, index, amount - coins[index], memo)
    exclude = coinChange(coins, index + 1, amount, memo)

    memo[index][amount] = min(include, exclude)
    return memo[index][amount]


def minCoins(coins, amount):
    memo = [[-1 for i in range(amount+1)]for j in range(len(coins)+1)]
    
    result = coinChange(coins, 0, amount, memo)
    return -1 if result == float('inf') else result


coins = [1, 2, 5]
amount = 11
print(minCoins(coins, amount))  # Output: 3
