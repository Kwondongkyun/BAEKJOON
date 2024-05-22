T=int(input())
l=[25,10,5,1]

for i in range(T):
    r=[0]*4
    C=int(input())
    for i in range(len(l)):
        r[i]+=C//l[i]
        C%=l[i]
    print(' '.join(str(x) for x in r))