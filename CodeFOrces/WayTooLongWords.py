def wayTooLong(letter):
    if len(letter)<=10:
        return letter
    return letter[0]+str(len(letter)-2)+letter[-1]



n=int(input())
for i in range(n):
    val=input()
    print(wayTooLong(val))