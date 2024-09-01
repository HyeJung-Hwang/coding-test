# 이것이 취업을 위한 코딩테스트다.
# 시각
import time

start_time = time.time()
N = int(input())
start_hour, start_minute, start_second = 0,0,0
end_hour, end_minute, end_second = N,59,59

count = 0
for hour in range(start_hour, end_hour + 1):
    for minute in range(start_minute,end_minute +1):
        for second in range(start_second,end_second + 1):
            clock = str(hour) + str(minute) + str(second)
            if "3" in clock:
                count += 1
print(count)
end_time = time.time()
print(f'Execution time: {end_time - start_time} seconds')