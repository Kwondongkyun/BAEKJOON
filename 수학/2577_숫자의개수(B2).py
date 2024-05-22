a=int(input())
b=int(input())
c=int(input())
l=[0]*10

n=list(map(int, str(a*b*c)))

for i in range(len(n)):
    l[n[i]]+=1
for i in range(len(l)):
    print(l[i])



