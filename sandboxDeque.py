# learning how to use the deque
from collections import deque

x = deque()
print(x)

x.append(10)
x.append(50)
x.append(100)
print(x.popleft())
