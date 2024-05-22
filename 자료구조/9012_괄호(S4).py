# t=int(input())

# for i in range(t):
#     stack=[]
#     a=input()
#     for j in a:
#         if j=='(':
#             stack.append(j)
#         elif j==')':
#             if stack:
#                 stack.pop()
#             else:
#                 print("NO")
#                 break
#     else:
#         if not stack:
#             print("YES")
#         else:
#             print("NO")


t=int(input())

for i in range(t):
    l=[]
    a=input()
    for j in a:
        if j=='(':
            l.append(j)
        elif j==')':
            if l:
                l.pop()
            # l 리스트안에 '('이 없을때
            # ')'가 먼저 오면 안된다.
            else:
                print('NO')
                break
    else:
        # 괄호 쌍을 다 찾고 리스트 l이 비었을 때
        if not l:
            print("YES")
        # 리스트 안에 '('이 남아있을경우
        else:
            print("NO")
