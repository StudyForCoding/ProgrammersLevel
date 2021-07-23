# 카펫
def solution(brown, yellow):
    answer = []
    tmp = int((brown - 4)/2)
    for i in range(tmp):
        if i * (tmp - i) == yellow:
            answer = [tmp-i + 2 , i + 2]
            return answer
        
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.11ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.1MB)
# 테스트 7 〉	통과 (0.10ms, 10.2MB)
# 테스트 8 〉	통과 (0.12ms, 10.3MB)
# 테스트 9 〉	통과 (0.11ms, 10.2MB)
# 테스트 10 〉	통과 (0.13ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.00ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)