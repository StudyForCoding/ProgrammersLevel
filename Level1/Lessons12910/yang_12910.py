# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    if len(answer) == 0:
        answer = [-1]
    answer.sort()
    
    return answer
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (3.41ms, 13.4MB)
# 테스트 7 〉	통과 (0.29ms, 10.3MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.18ms, 10.3MB)
# 테스트 10 〉	통과 (0.13ms, 10.1MB)
# 테스트 11 〉	통과 (0.05ms, 10.3MB)
# 테스트 12 〉	통과 (0.05ms, 10.2MB)
# 테스트 13 〉	통과 (0.42ms, 10.3MB)
# 테스트 14 〉	통과 (0.17ms, 10.3MB)
# 테스트 15 〉	통과 (0.14ms, 10.3MB)
# 테스트 16 〉	통과 (0.04ms, 10.2MB)