# # 풀이 1
# a=int(input())
# b=int(input())
# c=0

# d=b%10
# print(a*d)
# c+=a*d

# e=int((b-d)/10)%10
# print(a*e)
# c+=a*e*10

# f=int(b/100)
# print(a*f)
# c+=a*f*100

# print(c)


# 풀이 2
a=int(input())
b=input()

num1 = a*int(b[2])
num2 = a*int(b[1])
num3 = a*int(b[0])
num4 = 100*num3+10*num2+num1

print(f"{num1}\n{num2}\n{num3}\n{num4}")
