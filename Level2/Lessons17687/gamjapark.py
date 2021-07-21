# [3차] n진수 게임

import string
tmp = string.digits+string.ascii_uppercase[:6]

def convert(n, base):
    q, r = divmod(n, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]
    
def solution(n, t, m, p):
    answer, nums = '', ''
    count, cur = 0, 0
    while count < t * m:
        num = convert(cur,n)
        nums += num
        count += len(num)
        cur += 1

    for i in range(p-1, count, m):
        answer += nums[i]
    return answer[:t]

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.11ms, 10.3MB)
테스트 6 〉	통과 (0.11ms, 10.4MB)
테스트 7 〉	통과 (0.21ms, 10.3MB)
테스트 8 〉	통과 (0.14ms, 10.3MB)
테스트 9 〉	통과 (0.12ms, 10.2MB)
테스트 10 〉	통과 (0.14ms, 10.3MB)
테스트 11 〉	통과 (0.14ms, 10.3MB)
테스트 12 〉	통과 (0.16ms, 10.3MB)
테스트 13 〉	통과 (0.14ms, 10.3MB)
테스트 14 〉	통과 (24.25ms, 10.4MB)
테스트 15 〉	통과 (24.34ms, 10.4MB)
테스트 16 〉	통과 (22.35ms, 10.4MB)
테스트 17 〉	통과 (1.03ms, 10.2MB)
테스트 18 〉	통과 (1.30ms, 10.3MB)
테스트 19 〉	통과 (0.36ms, 10.3MB)
테스트 20 〉	통과 (1.15ms, 10.4MB)
테스트 21 〉	통과 (6.58ms, 10.3MB)
테스트 22 〉	통과 (2.70ms, 10.3MB)
테스트 23 〉	통과 (8.42ms, 10.3MB)
테스트 24 〉	통과 (11.47ms, 10.4MB)
테스트 25 〉	통과 (10.08ms, 10.3MB)
테스트 26 〉	통과 (3.43ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''