n=int(input())
coin_list=[5,2]
count=0

while n>=0:
    if n%5==0:
        count+=n//5
        n%=5
        print(count)
        break
    else:
        n-=2
        count+=1

else:
    print(-1)


# for coin in coin_list:
#     count+=n//coin
#     n%=coin
# print(count)

while n>=0:
    if n%5==0:
        count+=n//5
        n%=5
        print(count)
        break
    else:
        n-=2
        count+=1

else:
    print(-1)
