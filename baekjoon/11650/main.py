import sys
from queue import PriorityQueue

n = int(sys.stdin.readline().rstrip())
list_coord = PriorityQueue()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    list_coord.put((x, y))

while not list_coord.empty():
    x, y = list_coord.get()
    print(x, y)
