def find(x):
  if p[x] != x:
    p[x] = find(p[x])
  return p[x]

def merge(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    if s[x] > s[y]:
      p[y] = x
      s[x] += s[y]
    else:
      p[x] = y
      s[y] += s[x]

#n, k = map(int, input().split())
n,k=5,3
p = list(range(n))
s = [1]*n
m = [False]*n


e=[(2 ,1 ,5),(1,0,8),(2,4,5),(1,3,4)]
# for _ in range(n-1):
#   x, y, r = map(int, input().split())
#   e.append((r, x, y))

# for _ in range(k):
#   i = int(input())
#   m[i] = True
m[2]=True
m[4]=True
m[0]=True
e = sorted(e, reverse=True)
c = 0

for ( x, y,r) in e:
  x = find(x)
  y = find(y)
  if not (m[x] and m[y]):
    merge(x, y)
    m[x] = m[x] or m[y]
    m[y] = m[x]
  else:
    c += r

print(c)