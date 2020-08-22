def romanDecimal(arr):
    dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    res=0
    for i in range(len(arr)-1):
        if dict[arr[i]]<dict[arr[i+1]]:
            res-=dict[arr[i]]
        else:
            res+=dict[arr[i]]
    res+=dict[arr[len(arr)-1]]
    return res



arr="III"
print(romanDecimal(arr))