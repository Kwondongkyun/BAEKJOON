a=[0]*10
b=[0]*42
c=0

for i in range(10):
    a[i]=int(input())
    b[a[i]%42]+=1

for i in range(len(b)):
    if(b[i]!=0):
        c+=1
print(c)



# l= [0] * 42
# for _ in range(10):
#     t= int(input())
#     l[t%42]=1
# print(sum(l))