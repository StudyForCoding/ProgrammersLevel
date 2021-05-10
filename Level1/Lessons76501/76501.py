# 음양 더하기   
def solution(absolutes, signs):
    answer = 0
    for value, sign in zip(absolutes, signs):
        answer += value * (sign * 2 - 1)
    return answer

# 테스트 1 〉	통과 (0.15ms, 10.2MB)
# 테스트 2 〉	통과 (0.18ms, 10.3MB)
# 테스트 3 〉	통과 (0.16ms, 10.2MB)
# 테스트 4 〉	통과 (0.17ms, 10.2MB)
# 테스트 5 〉	통과 (0.17ms, 10.4MB)
# 테스트 6 〉	통과 (0.14ms, 10MB)
# 테스트 7 〉	통과 (0.16ms, 10.1MB)
# 테스트 8 〉	통과 (0.16ms, 10.1MB)
# 테스트 9 〉	통과 (0.16ms, 10.2MB)