# 이것이 취업을 위한 코딩테스트다.
# 상하좌우
import time

start_time = time.time()
N = int(input())
moving_plan = list(input().split())

now = [1,1]
moving_dict = {
    "R":(0,1),
    "L":(0,-1),
    "U":(-1,0),
    "D":(1,0)
}
for plan in moving_plan:
    dx, dy = moving_dict[plan]
    temp_x,temp_y =  now[0] + dx, now[1] + dy

    # 공간 안에서만 이동 가능한 경우에만 업데이트 아닌 경우는 패스
    if 1<= temp_x <= 5 and  1<= temp_y <= 5 :
        now[0] = temp_x
        now[1] = temp_y

print(now)
end_time = time.time()
print(f'Execution time: {end_time - start_time} seconds')


    

