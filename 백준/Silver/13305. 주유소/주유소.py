t = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
pay = 0

for i in range(t-1):
    if min_cost >= cost[i]:
        min_cost = cost[i]
    pay += dist[i] * min_cost

print(pay)