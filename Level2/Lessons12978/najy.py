# 배달
def solution(N, road, K):
    answer = 0
    dsts = [[K+1 for i in range(N)] for j in range(N)]
    
    for i in range(N):
        dsts[i][i] = 0
    
    for p in road:
        if dsts[p[1]-1][p[0]-1] > p[2]:
            dsts[p[1]-1][p[0]-1] = p[2]
            dsts[p[0]-1][p[1]-1] = p[2]
            
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dsts[j][k] > dsts[j][i] + dsts[i][k]:
                    dsts[j][k] = dsts[j][i] + dsts[i][k]
    
    for i in range(N):
        if dsts[0][i] <= K:
            answer += 1
    
    return answer
'''
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.27ms, 10.2MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.21ms, 10.3MB)
테스트 11 〉	통과 (0.28ms, 10.3MB)
테스트 12 〉	통과 (8.17ms, 10.2MB)
테스트 13 〉	통과 (5.48ms, 10.2MB)
테스트 14 〉	통과 (5.07ms, 10.3MB)
테스트 15 〉	통과 (8.10ms, 10.3MB)
테스트 16 〉	통과 (1.41ms, 10.3MB)
테스트 17 〉	통과 (4.28ms, 10.2MB)
테스트 18 〉	통과 (16.88ms, 10.3MB)
테스트 19 〉	통과 (15.35ms, 10.3MB)
테스트 20 〉	통과 (17.46ms, 10.2MB)
테스트 21 〉	통과 (11.67ms, 10.4MB)
테스트 22 〉	통과 (17.91ms, 10.3MB)
테스트 23 〉	통과 (18.77ms, 10.4MB)
테스트 24 〉	통과 (14.89ms, 10.5MB)
테스트 25 〉	통과 (19.45ms, 10.6MB)
테스트 26 〉	통과 (30.62ms, 10.5MB)
테스트 27 〉	통과 (15.17ms, 10.5MB)
테스트 28 〉	통과 (18.17ms, 10.5MB)
테스트 29 〉	통과 (19.71ms, 10.6MB)
테스트 30 〉	통과 (20.02ms, 10.6MB)
테스트 31 〉	통과 (19.48ms, 10.3MB)
테스트 32 〉	통과 (18.49ms, 10.3MB)
'''