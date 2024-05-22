# 내 풀이
T=int(input())

b=[300, 60, 10]
count=[0]*3

if T%10!=0:
    print(-1)

else:
    for i in range(len(b)):
        if(T//b[i]>0):
            count[i]+=T//b[i]
            T%=b[i]
        print(count[i], end=' ')
    

# # 다른 풀이
# T=int(input())

# b=[300, 60, 10]
# count=[0]*3

# if T%10!=0:
#     print(-1)

# else:
#     for button in b:
#         print(T//button, end=' ')
#         T=T%button