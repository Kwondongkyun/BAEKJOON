a, b=map(str, input().split())

for i in range(-1, -4, -1):
    if(a[i]>b[i]):
        t=list(reversed(a))
        print(''.join(str(x) for x in t))
        break

    elif(a[i]<b[i]):
        t=list(reversed(b))
        print(''.join(str(x) for x in t))
        break
    else:
        continue