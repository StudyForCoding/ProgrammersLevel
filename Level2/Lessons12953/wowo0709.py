# N개의 최소공배수

from math import gcd
def solution(arr):
    ans = arr[0]
    for nbr in arr:
        ans = ans*nbr // gcd(ans,nbr)

    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''