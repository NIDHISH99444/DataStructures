# In Little Flowers Public School, there are many students with same first names. You are given a task to find the students with same names. You will be given a string comprising of all the names of students and you have to tell the name and count of those students having same. If all the names are unique, print -1 instead.
# Note: We don't have to mention names whose frequency is 1.
# Input Format:
# The only line of input will have a string ‘str’ with space separated first names of students.
# Output Format:
# Print the names of students along with their count if they are repeating. If no name is repeating, print -1
# Constraints:
# 1 <= |str| <= 10^5
# Time Limit: 1 second
# Sample Input 1:
# Abhishek harshit Ayush harshit Ayush Iti Deepak Ayush Iti
# Sample Output 1:
# harshit 2
# Ayush 3
# Iti 2
# Sample Input 2:
# Abhishek Harshit Ayush Iti
# Sample Output:
# -1


def repeatingNames(arr):
    hs={}
    for ele in arr:
        if ele not in hs:
            hs[ele]=1
        else:
            hs[ele]+=1
    for ele in arr:
        if hs[ele] ==1 :
            del hs[ele]
    return (hs)

#
# n=[ele for ele in input().split()]
# repeatingNames(n)
# #Abhishek harshit Ayush Iti Deepak
str="Abhishek harshit Ayush Iti Deepak"
names=str.strip().split()
m=repeatingNames(names)

if m:
    for name in m:
        print(name, m[name])
else:
    print(-1)