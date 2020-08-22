def maxProfit(price,lengthOfRod):

    n=lengthOfRod
    t=[[0 for i in range(n+1)]for j in range(len(price)+1)]
    for i in range(1,len(t)):
        for j in range(1,len(t[0])):
            if i<=j:
                t[i][j]=max(t[i-1][j] ,price[i-1]+t[i][j-i])
            else:
                t[i][j]=t[i-1][j]
    print(t[-1][-1])

lengthOfRod=5
price=[2,5,7,8]
#price=[1,5,8,9,10,17,17,20]
maxProfit(price,lengthOfRod)
#
# # A Dynamic Programming solution for Rod cutting problem
# INT_MIN = -32767
#
# # Returns the best obtainable price for a rod of length n and
# # price[] as prices of different pieces
# def cutRod(price, n):
# 	val = [0 for x in range(n+1)]
# 	val[0] = 0
#
# 	# Build the table val[] in bottom up manner and return
# 	# the last entry from the table
# 	for i in range(1, n+1):
# 		max_val = INT_MIN
# 		for j in range(i):
# 			max_val = max(max_val, price[j] + val[i-j-1])
# 		val[i] = max_val
#
# 	return val[n]
#
# # Driver program to test above functions
# arr = [1, 5, 8, 9, 10, 17, 17, 20]
# size = len(arr)
# print("Maximum Obtainable Value is " + str(cutRod(arr, size)))

# This code is contributed by Bhavya Jain
