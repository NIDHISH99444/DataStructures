


def rodCutting(length,price,W):
    matrix=[[0 for i in range(W+1)]for j in range(len(length)+1)]
    for i in range(1,W+1):
        for j in range(1,len(length)+1):
            if length[i-1]<=j:
                matrix[i][j]=max(matrix[i-1][j],price[i-1]+matrix[i][j-length[i-1]])
            else:
                matrix[i][j]=matrix[i-1][j]
    return (matrix[-1][-1])
W=8
length=[1,2,3,4,5,6,7,8]
price=[1 ,  5 ,  8 ,  9 , 10 , 17 , 17 , 20]
print(rodCutting(length,price,W))