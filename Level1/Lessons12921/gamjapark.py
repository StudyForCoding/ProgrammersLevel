# 소수 찾기

def prime_list(n):
    arr = [1 for i in range(n+1)]
    for i in range(2, int(n**0.5)  + 1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = 0
    return arr

def solution(n):
    answer = sum(prime_list(n)) - 2
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.16ms, 10.3MB)
테스트 5 〉	통과 (0.10ms, 10.3MB)
테스트 6 〉	통과 (1.18ms, 10.3MB)
테스트 7 〉	통과 (0.38ms, 10.3MB)
테스트 8 〉	통과 (0.99ms, 10.3MB)
테스트 9 〉	통과 (1.57ms, 10.3MB)
테스트 10 〉	통과 (30.72ms, 12.1MB)
테스트 11 〉	통과 (102.58ms, 16.8MB)
테스트 12 〉	통과 (34.75ms, 12.5MB)
효율성  테스트
테스트 1 〉	통과 (128.57ms, 17.3MB)
테스트 2 〉	통과 (105.49ms, 17.1MB)
테스트 3 〉	통과 (108.78ms, 17.1MB)
테스트 4 〉	통과 (108.40ms, 17.2MB)
채점 결과
정확성: 75.0
효율성: 25.0
합계: 100.0 / 100.0
'''