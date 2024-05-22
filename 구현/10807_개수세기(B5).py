n=int(input())
l=list(map(int, input().split(' ')))
m=int(input())
cnt=0

for _ in range(len(l)):
    if(l[_]==m):
        cnt+=1
print(cnt)