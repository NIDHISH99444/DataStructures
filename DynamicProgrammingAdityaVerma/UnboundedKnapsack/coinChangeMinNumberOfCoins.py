from sys import  maxsize
def coinChange( coins, amount):
    t = [[0 for i in range(amount + 1)] for j in range(len(coins) + 1)]
    for i in range(1,len(t[0])):
        t[0][i]=maxsize
    for i in range(1,len(t)):
        for j in range(1,len(t[0])):
            if coins[i-1]<=j :
                t[i][j]=min(t[i-1][j],1+t[i][j-coins[i-1]])
            else:
                t[i][j]=t[i-1][j]
    return (t)

coins = [1, 2, 5]
amount = 11
print(coinChange(coins,amount))