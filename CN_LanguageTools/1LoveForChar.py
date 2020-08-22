# Ayush loves the characters ‘a’, ‘s’, and ‘p’. He got a string of lowercase letters and he wants to find out how many times characters ‘a’, ‘s’, and ‘p’ occurs in the string respectively. Help him find it out.
# Input:
# First line contains an integer denoting length of the string.
# Next line contains the string.
# Constraints:
# 1<=n<=10^5
# ‘a’<= each character of string <= ‘z’
# Output:
# Three space separated integers denoting the occurrence of letters ‘a’, ‘s’ and ‘p’ respectively.
# Sample Input:
# 6
# aabsas
# Sample output:
# 3 2 0

def loveForChar(arr):
    hs={}
    for char in ["a","s","p"]:
        hs[char]=0
    for i in range(len(arr)):
        if arr[i] in hs:
            hs[arr[i]]+=1
    for ele in hs.values():
        print(ele,end=" ")
n=int(input())
p=input()
loveForChar(p)

#18
#owbdmvoechwwgunmrt
#6
#vfefgk
#36
#yndatfuqmzctvbyttrsfafmhkavwgqeuyoxo
#3 1 0
