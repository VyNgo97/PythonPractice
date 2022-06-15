'''
It is recommended to use deque from collections rather than lists for queues.
'''

from collections import deque

queue = deque(['vy', 'jamie', 'orion', 'luna'])

# appends to the end of the queue
queue.append('chicken')

# removes the first element added to the queue
queue.popleft()

print(queue)