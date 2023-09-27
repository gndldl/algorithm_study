import heapq
import sys

input = sys.stdin.readline

n = int(input())

time_list = []
for _ in range(n):
    time_list.append(list(map(int, input().split())))

time_list.sort()

temp = 0

classes = []

for start, end in time_list:
    if not classes:
        heapq.heappush(classes, end)
    else:
        if start < classes[0]:
            heapq.heappush(classes, end)
        else:
            heapq.heappop(classes)
            heapq.heappush(classes, end)

print(len(classes))