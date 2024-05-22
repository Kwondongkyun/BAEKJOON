# # 풀이 1
# n=int(input())
# m=1000000
# M=0
# a = list(map(int, input().split()))

# a.sort()
# print(f"{a[0]} {a[n-1]}")


#(시간 복잡도 줄이기)
# 풀이 2
n=int(input())
a = list(map(int, input().split()))
m=a[0]
M=a[0]

# m=1000000, M=0으로 잡고 했을때는 왜 오류가 나지?

for i in range(n):
    if(a[i]<m):
        m=a[i]
    elif(a[i]>M):
        M=a[i]

print(m,M)