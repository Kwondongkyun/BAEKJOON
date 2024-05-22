l=[]
max=0
idx=0
for i in range(9):
    l.append(int(input()))
    if(max<l[i]):
        max=l[i]
        idx=i+1
print(f"{max}\n{idx}")