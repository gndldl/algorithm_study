n = int(input())
# 각 팀 점수
score = {1: 0, 2: 0}
# 이기기 시작한 시간
time = {1: 0, 2: 0}
# 정답 제출 용
ans = {1: 0, 2: 0}
# 어느팀이 이기고 있는지를 나타내는 변수
state = 0


for _ in range(n):
    team, t = input().split()
    team = int(team)
    m, s = map(int, t.split(':'))
    t = m*60+s
    score[team] += 1
    # 비기고있다가 이기기 시작
    if state == 0:
        time[team] = t
        state = team
    # 이기고 있다가 비기게 됨
    elif state != 0 and score[1] == score[2]:
        ans[state] += t-time[state]
        state = 0
# 마지막 계산
if state != 0:
    ans[state] += 60*48-time[state]

print('{:0>2}:{:0>2}'.format(ans[1]//60, ans[1] % 60))
print('{:0>2}:{:0>2}'.format(ans[2]//60, ans[2] % 60))