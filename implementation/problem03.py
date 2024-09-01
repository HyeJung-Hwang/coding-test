# 이것이 취업을 위한 코딩 테스트다.
# 왕실의 나이트
import time

start_time = time.time()
# 시작 좌표 셋팅
now = list(input())
alphabet = "abcdefgh"
now[1],now[0]  = alphabet.find(now[0]) + 1,int(now[1])


count = 0
# 수직 -> 수평
## 수직 위로
for dx in [-2,2]:
    if 1 <= now[0] + dx <= 8:
        for dy in [-1,1]:
            if 1 <= now[1] + dy <= 8:
                count += 1
# 수평 -> 수직
for dy in [-2,2]:
    if 1 <= now[1] + dy<= 8:
        for dx in [-1,1]:
            if 1 <= now[0] + dx <= 8:
                count += 1
print(count)
end_time = time.time()
print(f"Time elapsed: {end_time-start_time}")