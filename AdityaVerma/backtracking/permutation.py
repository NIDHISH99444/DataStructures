input="abc"
output=""

def permute(input,output,res):
    if len(input)==0:
        res.append(output)
    for i in range(len(input)):
        permute(input[:i]+input[i+1:],output+input[i],res)




res=[]
permute(input,output,res)
print(res)    
