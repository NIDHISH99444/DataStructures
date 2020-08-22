
def knapsack(W,wt,val):
    t=[[0 for i in range(W+1)]for j in range(len(wt)+1)]

    for i in range(1,len(wt)+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                t[i][j]=max(t[i-1][j],val[i-1]+t[i-1][j-wt[i-1]])
            else:
                t[i][j]=t[i-1][j]
    print(t[-1][-1])



val= [60, 100, 120]
wt = [10, 20, 30]
W = 50

# val = [10, 20, 30, 40]
# wt = [12, 13, 15, 19]
# W = 10
knapsack(W,wt,val)