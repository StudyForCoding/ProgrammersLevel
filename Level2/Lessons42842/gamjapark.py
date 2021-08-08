# 카펫
def solution(brown, yellow):
    for i in range(1,int(yellow**0.5)+1):
        a, b = i + 2 , yellow//i + 2
        new_br = a*2 + b*2 - 4
        if new_br == brown and a * b == brown + yellow:
            break
    return [b, a]

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.36ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.12ms, 10.3MB)
테스트 7 〉	통과 (0.21ms, 10.3MB)
테스트 8 〉	통과 (0.33ms, 10.3MB)
테스트 9 〉	통과 (0.30ms, 10.3MB)
테스트 10 〉	통과 (0.39ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''