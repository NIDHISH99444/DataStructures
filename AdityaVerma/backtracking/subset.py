nums=[1,2,3]

def subsets( input,output,res):
    if len(input)==0:
        res.append(output)
        return 
    subsets(input[1:],output,res)
    subsets(input[1:],output+[input[0]],res)


output=[]
res=[]
subsets(nums,output,res)
print(res)