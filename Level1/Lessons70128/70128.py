# 내적
def solution(a, b):
    answer = 0
    for x,y in zip(a,b):
      answer += x * y
    return answer

# 테스트 1 〉	통과 (0.12ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.07ms, 10.2MB)
# 테스트 7 〉	통과 (0.09ms, 10.2MB)
# 테스트 8 〉	통과 (0.12ms, 10.2MB)
# 테스트 9 〉	통과 (0.12ms, 10.4MB)