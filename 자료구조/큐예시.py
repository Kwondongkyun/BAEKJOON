from collections import deque
queue=deque('asd')
queue.append('k')

print(queue) # deque(['a', 's', 'd', 'k'])
queue.popleft()
print(queue) # deque(['s', 'd', 'k'])

