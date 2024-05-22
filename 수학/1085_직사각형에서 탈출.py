x,y,w,h=map(int, input().split())
print(min(min(w-x, h-y),x,y))