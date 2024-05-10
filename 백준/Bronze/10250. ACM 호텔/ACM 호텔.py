t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n%h
    no = n//h + 1
    
    if floor == 0:
        floor = h
        no -= 1
    
    print(floor * 100 + no)
