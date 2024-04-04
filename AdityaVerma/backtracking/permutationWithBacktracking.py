string= [1,1,2]
def permute(string,start,res):
    if start==len(string)-1:
        res.append(list(string))
    for i in range(start,len(string)):
        string[start],string[i]=string[i],string[start]
        permute(string,start+1,res)
        string[start],string[i]=string[i],string[start]


res=[]
permute(string,0,res)
print(res)    
