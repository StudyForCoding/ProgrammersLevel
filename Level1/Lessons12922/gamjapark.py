#수박수박수박수박수박수?

def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.17ms, 10.2MB)
테스트 2 〉	통과 (0.82ms, 10.1MB)
테스트 3 〉	통과 (0.30ms, 10.1MB)
테스트 4 〉	통과 (0.89ms, 10.3MB)
테스트 5 〉	통과 (0.47ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (1.36ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
