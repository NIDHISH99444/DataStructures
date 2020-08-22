# There is only one beauty parlour in the town CodingNinjasLand. The receptionist at the beauty parlor is flooded with appointment requests because the “Hakori” festival is round the corner and everyone wants to look good on it.
# She needs your help. The problem is they don’t have chairs in reception. They are ordering chairs from NinjasKart. They don’t want to order more than required. You have to tell the minimum number of chairs required such that none of the customers has to stand.
# Input Format :
# First line contains the number of customers that will come. Second line contains N space-separated integers which represent the arrival timings of the customer. Third line contains N space-separated integers which represent the departure timings of the customer. Arrival and departure timings are given in 24-hour clock.
# Constraints:
# 1<= N <= 100
# Arrival and departure timings lie in the range [0000 to 2359]
# Time Limit: 1 second
# Output Format :
# You have to print the minimum number of chairs required such that no customer has to wait standing.
# Sample Test Cases:
# Sample Input 1 :
# 5
# 900 1000 1100 1030 1600
# 1900 1300 1130 1130 1800
# Sample Output 1:
# 4
# Explanation:
# 4 because at 1100 hours, we will have maximum number of customers at the shop, throughout the day. And that maximum number is 4.


def warmReception(arrival,departure):
    arrival.sort()
    departure.sort()
    res=0
    i,j=1,0
    # count=1
    # while i<len(arrival) and j < len(departure):
    #     if arrival[i]<=departure[j]:
    #         count+=1
    #         i+=1
    #         res=max(res,count)
    #     else:
    #         count-=1
    #         j+=1
    # return res
    cnt=1
    maxCount=1
    while i< len(arrival):
        if arrival[i]<=departure[j]:
            cnt+=1
            maxCount=max(maxCount,cnt)
            i+=1
        else:
            cnt-=1
            j+=1
    return  maxCount



arrival=list(map(int,input().split()))
departure=list(map(int,input().split()))
print(warmReception(arrival,departure))

# 8
# 307 2007 1736 2314 2101 1719 435 2214
# 400 2100 1800 2359 2200 1800 500 2300
# 10
# 1700 1607 2212 605 605 1 1002 127 2304 1013
# 1900 1900 2300 1800 1700 500 1100 1000 2359 1100
# 9
# 1708 1607 2012 605 605 101 1002 127 2304
# 1900 1800 2300 1800 1700 1500 1200 1200 2359
# 10
# 1708 1607 2212 605 605 101 1002 127 2304 1013
# 1900 1900 2300 1800 1700 1500 1200 1200 2359 1200
# 2,4,5,6