import sys
input=sys.stdin.readline
n=int(input())
stack=[]

for _ in range(n):
    cmd=list(input().split())

    if cmd[0]=='push':
        stack.append(cmd[1])
    
    if cmd[0]=='pop':
        if(len(stack)>0):
            print(stack.pop(-1))
        else: print(-1)

    if cmd[0]=='size':
        print(len(stack))
    
    if cmd[0]=='empty':
        print(1 if len(stack)==0 else 0)
    
    if cmd[0]=='top':
        if(len(stack)>0):
            print(stack[-1])
        else: print(-1)