# # 풀이1 - str
# n=input()
# count=0
# l=n

# while(1):
#     if len(l)==1:
#         l='0'+l
#     p=str((int(l[0])+int(l[1])))
#     l=l[-1]+p[-1]
#     print(l)
#     count+=1
#     if(l==n):
#         print(count)
#         break

# 풀이 2
n=int(input())
cnt=0
m=n

while(1):
    m=(m%10)*10 + (int(m/10)+m%10)%10
    cnt+=1
    if(m==n):
        print(cnt)
        break

