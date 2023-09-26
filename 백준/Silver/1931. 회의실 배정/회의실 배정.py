#입력
n = int(input())
s = []
for i in range(n):
    st, end = map(int, input().split())
    s.append((st,end))
    
#2차원 배열 sort (시작시간순 1번, 종료시간순 2번)
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])

#i의 시작시간이 종료시간보다 빠르면, endt = i의 종료시간
endt = 0
count = 0
for i in s:
    if i[0] >= endt:
        endt = i[1]
        count+=1
print(count)