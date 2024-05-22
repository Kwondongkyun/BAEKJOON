# 풀이 1
N=int(input())
a=list(map(int, input().split()))
m=max(a)
b=0

for i in range(N):
    a[i]=a[i]/m*100
    b+=a[i]

print(b/N)


# 시간복잡도 더 크다.
# 풀이 2
N=int(input())
a=list(map(int, input().split()))
m=max(a)

for i in range(N):
    a[i]=a[i]/m*100

print(sum(a)/N)
