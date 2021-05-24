# 내적

def solution(a, b):
    answer=0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

"""
테스트 1 〉	통과 (0.12ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.10ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.2MB)
테스트 8 〉	통과 (0.16ms, 10.3MB)
테스트 9 〉	통과 (0.15ms, 10.1MB)
"""