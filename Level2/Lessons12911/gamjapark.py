# 다음 큰 숫자
def Count(x):
    return sum(list(map(int, str(bin(x))[2:])))
def solution(n):
    answer = 0
    count = Count(n)
    for i in range(n+1, 1000001):
        tmp = Count(i)
        if count == tmp:
            answer = i
            break
    return answer

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.5MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.04ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.07ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
채점 결과
정확성: 70.0
효율성: 30.0
합계: 100.0 / 100.0
'''
