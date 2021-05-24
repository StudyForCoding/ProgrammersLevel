# 실패율

def solution(N, stages):
    stages.sort()
    not_clear = {i:0 for i in range(1, N+1)}
    arrive = [0 for _ in range(N + 2)]
    for s in stages:
        for i in range(1, s + 1):
            arrive[i] += 1
        try: not_clear[s] += 1
        except: continue
    for i in range(1, N + 1):
        if arrive[i] == 0:
            not_clear[i] = 0
        else:
            not_clear[i] /= arrive[i]

    return sorted(not_clear, key=lambda x:-not_clear[x])

'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (1.16ms, 10.2MB)
테스트 3 〉	통과 (171.36ms, 10.4MB)
테스트 4 〉	통과 (859.55ms, 11.3MB)
테스트 5 〉	통과 (3205.10ms, 15.7MB)
테스트 6 〉	통과 (2.48ms, 10.3MB)
테스트 7 〉	통과 (29.79ms, 10.3MB)
테스트 8 〉	통과 (853.44ms, 11.2MB)
테스트 9 〉	통과 (3492.34ms, 15.7MB)
테스트 10 〉	통과 (361.92ms, 11.2MB)
테스트 11 〉	통과 (845.29ms, 11.2MB)
테스트 12 〉	통과 (360.82ms, 11.8MB)
테스트 13 〉	통과 (1741.30ms, 12MB)
테스트 14 〉	통과 (0.27ms, 10.2MB)
테스트 15 〉	통과 (88.64ms, 10.6MB)
테스트 16 〉	통과 (14.27ms, 10.3MB)
테스트 17 〉	통과 (79.46ms, 10.6MB)
테스트 18 〉	통과 (14.33ms, 10.3MB)
테스트 19 〉	통과 (3.76ms, 10.2MB)
테스트 20 〉	통과 (26.43ms, 10.4MB)
테스트 21 〉	통과 (44.74ms, 11MB)
테스트 22 〉	통과 (6961.56ms, 18.3MB)
테스트 23 〉	통과 (101.80ms, 12.1MB)
테스트 24 〉	통과 (195.77ms, 12.3MB)
테스트 25 〉	통과 (0.01ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
'''