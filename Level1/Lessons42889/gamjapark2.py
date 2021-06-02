# 실패율

def solution(N, stages):
    not_clear = {i:0 for i in range(1, N+2)}
    fail = {i:0 for i in range(1, N+1)}
    
    total_sum = 0
    for s in stages:
        total_sum += 1
        not_clear[s] = not_clear.get(s, 0) + 1
    
    for i in range(1, N + 1):
        if i >= 2:
            total_sum -= not_clear[i-1]
        if total_sum == 0:
            fail[i] = 0
        else:
            fail[i] = not_clear[i] / total_sum
    return sorted(fail, key=lambda x:-fail[x])

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.19ms, 10.2MB)
테스트 3 〉	통과 (1.93ms, 10.4MB)
테스트 4 〉	통과 (11.59ms, 10.8MB)
테스트 5 〉	통과 (25.25ms, 15MB)
테스트 6 〉	통과 (0.25ms, 10.2MB)
테스트 7 〉	통과 (1.50ms, 10.3MB)
테스트 8 〉	통과 (12.57ms, 10.8MB)
테스트 9 〉	통과 (26.83ms, 15MB)
테스트 10 〉	통과 (12.69ms, 10.9MB)
테스트 11 〉	통과 (12.06ms, 10.9MB)
테스트 12 〉	통과 (17.00ms, 11.4MB)
테스트 13 〉	통과 (20.51ms, 11.4MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (8.18ms, 10.6MB)
테스트 16 〉	통과 (4.58ms, 10.3MB)
테스트 17 〉	통과 (8.19ms, 10.6MB)
테스트 18 〉	통과 (4.15ms, 10.3MB)
테스트 19 〉	통과 (1.34ms, 10.3MB)
테스트 20 〉	통과 (6.00ms, 10.3MB)
테스트 21 〉	통과 (10.75ms, 11MB)
테스트 22 〉	통과 (26.82ms, 18.3MB)
테스트 23 〉	통과 (24.58ms, 11.6MB)
테스트 24 〉	통과 (23.65ms, 11.7MB)
테스트 25 〉	통과 (0.01ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
'''