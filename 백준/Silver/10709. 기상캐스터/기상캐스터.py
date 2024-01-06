h, w = map(int, input().split())

graph = []

for i in range(h):
    line = list(map(str,input()))
    check = False
    cnt = 0
    a = []
    for i in line:
        if i == 'c':
            a.append(0)
            check = True
            cnt = 0
        else:
            if check:
                cnt += 1
                a.append(cnt)
            else:
                a.append(-1)
            
    graph.append(a)

for i in graph:
    print(*i)