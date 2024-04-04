input=[1,2,1]
sum=2

def checkSum(input,output,sum,dp):
        if sum==0:
            return 1
        if sum<0:
            return 0 
            
        if len(input)==0:
            return 0
        if dp[len(input)][sum]!=-1:
             return dp[len(input)][sum]
        dp[len(input)][sum]= checkSum(input[1:],output,sum,dp)+ checkSum(input[0:],output+[input[0]],sum-input[0],dp)     
        return dp[len(input)][sum]
sum = 100
input = [3,5,7,8,9,10,11]
output=[]
dp=[[-1 for i in range(sum+1) ]for j in range(len(input)+1)]
print(checkSum(input,output,sum,dp))
