# 실패율

def solution(N, stages):
    not_clear = {i:0 for i in range(1, N+2)}
    fail = {i:0 for i in range(1, N+1)}
    
    for s in stages:
        not_clear[s] = not_clear.get(s, 0) + 1
    arrive = [not_clear[i] for i in range(1, N+2)]
    for i in range(N-1, -1, -1):
        arrive[i] += arrive[i + 1]
        
    for i in range(N):
        if arrive[i] == 0:
            fail[i+1] = 0
        else:
            fail[i+1] = not_clear[i+1] / arrive[i]
    return sorted(fail, key=lambda x:-fail[x])
'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.83ms, 10.2MB)
테스트 3 〉	통과 (1.78ms, 10.3MB)
테스트 4 〉	통과 (8.69ms, 10.9MB)
테스트 5 〉	통과 (22.47ms, 15MB)
테스트 6 〉	통과 (0.22ms, 10.2MB)
테스트 7 〉	통과 (1.31ms, 10.3MB)
테스트 8 〉	통과 (8.48ms, 10.8MB)
테스트 9 〉	통과 (21.84ms, 14.9MB)
테스트 10 〉	통과 (9.64ms, 11MB)
테스트 11 〉	통과 (9.56ms, 10.8MB)
테스트 12 〉	통과 (14.48ms, 11.5MB)
테스트 13 〉	통과 (15.41ms, 11.4MB)
테스트 14 〉	통과 (0.04ms, 10.3MB)
테스트 15 〉	통과 (5.97ms, 10.5MB)
테스트 16 〉	통과 (3.58ms, 10.3MB)
테스트 17 〉	통과 (6.41ms, 10.6MB)
테스트 18 〉	통과 (3.54ms, 10.4MB)
테스트 19 〉	통과 (1.06ms, 10.3MB)
테스트 20 〉	통과 (4.72ms, 10.5MB)
테스트 21 〉	통과 (9.08ms, 10.9MB)
테스트 22 〉	통과 (23.39ms, 18.1MB)
테스트 23 〉	통과 (18.84ms, 11.7MB)
테스트 24 〉	통과 (17.20ms, 11.6MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.1MB)
'''