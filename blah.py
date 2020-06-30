import heapq
import random

x = random.sample(range(1,11), 10)
print(x)
heapq.heapify(x)
print(x)