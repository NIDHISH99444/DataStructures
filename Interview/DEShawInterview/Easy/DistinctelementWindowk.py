def countDistinct(arr,k):
    res=[]
    dict={}
    for i in range(k):
        if arr[i] in dict:
            dict[arr[i]]+=1
        else:
            dict[arr[i]]=1
    res.append(len(dict.keys()))
    for i in range(k,len(arr)):
        dict[arr[i-k]]-=1
        if dict[arr[i-k]]==0:
            del dict[arr[i-k]]
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1
        res.append(len(dict.keys()))

    return  res


arr=[1, 2, 1, 3, 4, 2, 3]
print(countDistinct(arr,4))