def change( amount, coins):
    t=[[0 for i in range(amount+1)]for j in range(len(coins)+1)]
    for i in range(len(t)):
        t[i][0]=1
    for i in range(1,len(t)):
        for j in range(1,len(t[0])):
            if coins[i-1]<=j :
                t[i][j]=t[i-1][j]+t[i][j-coins[i-1]]
            else:
                t[i][j]=t[i-1][j]
    print(t[-1][-1])






amount = 5
coins = [1, 2, 5]
change(amount,coins)