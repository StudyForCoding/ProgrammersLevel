# 음양 더하기
absolutes = [1,2,3]
signs = [False,False,True]
answer = 0

for idx,value in enumerate(absolutes):
    if signs[idx]:
        answer += value
    else:
        answer -= value

print(answer)

"""
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.14ms, 10.2MB)
테스트 3 〉	통과 (0.12ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.13ms, 10.1MB)
테스트 6 〉	통과 (0.11ms, 10.2MB)
테스트 7 〉	통과 (0.12ms, 10.2MB)
테스트 8 〉	통과 (0.14ms, 10.3MB)
테스트 9 〉	통과 (0.14ms, 10.4MB)
"""