hour, minute = map(int, input().split())

# 분 단위가 45분 보다 작을 때
# 분이 45보다 크다면 입력받은 hour시 minute분에서 바로 45를 뻄
if minute < 45: # 분 단위가 45분 보다 작을 때
    if hour == 0:   # 0 시 일경우
        hour = 23
        minute += 60
    else:           # 0 시가 아니면
        hour -= 1
        minute += 60
print(hour, minute - 45)