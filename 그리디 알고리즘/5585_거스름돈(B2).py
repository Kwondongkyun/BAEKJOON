x=int(input())
x=1000-x
c=[500,100,50,10,5,1]
count=0

for coin in c:
    count+=x//coin
    x%=coin
print(count)