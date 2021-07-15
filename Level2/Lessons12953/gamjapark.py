# N개의 최소공배수

import math
def lcm(a,b):
    return int(abs((a*b)/math.gcd(a,b)))
def solution(arr):
    if len(arr) == 1:
        return arr[0]
    arr.sort()
    result = lcm(arr[0], arr[1])
    for i in range(2,len(arr)):
        result = lcm(result, arr[i])
    return result
    
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
