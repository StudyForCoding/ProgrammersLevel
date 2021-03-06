# 두 정수 사이의 합
def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a,b+1))
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (311.90ms, 10.2MB)
테스트 5 〉	통과 (194.25ms, 10.1MB)
테스트 6 〉	통과 (158.94ms, 10.2MB)
테스트 7 〉	통과 (89.64ms, 10MB)
테스트 8 〉	통과 (144.47ms, 10.2MB)
테스트 9 〉	통과 (99.75ms, 10.2MB)
테스트 10 〉	통과 (21.62ms, 10.2MB)
테스트 11 〉	통과 (0.15ms, 9.98MB)
테스트 12 〉	통과 (0.44ms, 10.2MB)
테스트 13 〉	통과 (0.20ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.1MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.09ms, 10.1MB)
'''