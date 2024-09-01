# 이것이 취업을 위한 코딩테스트다
# 문자열 재정렬
import time

start_time = time.time()
input = input()

result_string = []
result_number = 0 
for char in input:
    if char.isalpha():
        result_string.append(char) 
    else:
        result_number += int(char)
result_string.sort()
print("".join(result_string) + str(result_number))
end_time = time.time()
print(f"Time elapsed: {end_time-start_time}")