def findFirstStream(arr):

    lst=[]
    dict={}
    for i in range(len(arr)):
        if arr[i] not in dict:
            dict[arr[i]]=1
            lst.append(arr[i])
        else:
            dict[arr[i]]+=1

        while len(lst)!=0:
            if dict[lst[0]]>1 :
                lst.pop(0)
            else:
                print(lst[0])
                break
        if len(lst)==0:
            print(-1)

stream="aqizqazpn"
findFirstStream(stream)