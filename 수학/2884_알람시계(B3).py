h, m = map(int, input().split())

if(h==0):
    if(m-45>=0):
        print(f"{h} {m-45}")
    elif(m-45<0):
        h=23
        print(f"{h} {60-(45-m)}")

else:
    if(m-45>=0):
        print(f"{h} {m-45}")
    elif(m-45<0):
        print(f"{h-1} {60-(45-m)}")