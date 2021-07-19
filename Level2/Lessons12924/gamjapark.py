# 숫자의 표현

def solution(n):
    answer = 0
    numSum = 0
    sNum = 1
    for i in range(1, n+1):
        numSum += i
        while numSum > n:
            numSum -= sNum
            sNum += 1
                
        if numSum == n:
            answer += 1
    return answer
    
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.13ms, 10.1MB)
테스트 3 〉	통과 (0.11ms, 10.1MB)
테스트 4 〉	통과 (0.11ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.10ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.20ms, 10.1MB)
테스트 11 〉	통과 (0.17ms, 10.1MB)
테스트 12 〉	통과 (0.11ms, 10.1MB)
테스트 13 〉	통과 (0.12ms, 10.1MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (1.63ms, 10.1MB)
테스트 2 〉	통과 (1.33ms, 10.2MB)
테스트 3 〉	통과 (1.42ms, 10.1MB)
테스트 4 〉	통과 (1.33ms, 10.2MB)
테스트 5 〉	통과 (1.40ms, 10.2MB)
테스트 6 〉	통과 (1.40ms, 10.2MB)
채점 결과
정확성: 70.0
효율성: 30.0
합계: 100.0 / 100.0
'''