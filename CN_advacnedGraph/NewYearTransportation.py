# int main(){
#     int n, t;
#     cin >> n >> t;
#
#     // int **graph = new int*[n];
#     // for(int i = 0; i < n; i++){
#     //     graph[i] = new int[n];
#     //     for(int j = 0; j < n; j++) graph[i][j] = 0;
#     // }
#
#     int position = 0;
#
#     for(int i = 0; i < n-1; i++){
#         if(position == t-1){
#             cout << "YES" << endl;
#             return 0;
#         }
#         int a;
#         cin >> a;
#         // graph[i][i+a] = 1;
#         if(i == position) position += a;
#     }
#
#     cout << "NO" << endl;
# }

# n,e=map(int,input().split())
# arr=(list(map(int,input().split())))
def check(arr,n,e):
    flag = 1
    pos=0
    for i in range(n - 1):
        pos += arr[i]
        if pos == e:
            flag = 0
            break
    if flag == 0:
        print("True")
    else:
        print("False")
n,e=8,4
arr=[1,2,1,2,1,1,1]


check(arr,n,e)




