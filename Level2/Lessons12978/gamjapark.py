# 배달
import sys
import heapq

def solution(N, road, K):
    road_map = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
    for r in road:
        road_map[r[0]][r[1]] = min(r[2], road_map[r[0]][r[1]])
        road_map[r[1]][r[0]] = min(r[2], road_map[r[0]][r[1]])

    answer = [sys.maxsize for _ in range(N+1)]
    answer[1] = 0
    tmp = []
    heapq.heappush(tmp, [0, 1])
    while tmp:
        dis,v  = heapq.heappop(tmp)
        for i in range(1, N+1):
            new_dis = road_map[v][i] + dis
            if new_dis < answer[i] and new_dis <= K:
                answer[i] = new_dis
                heapq.heappush(tmp, [new_dis, i])
    ret = 0
    for i in range(1, N+1):
        if answer[i] != sys.maxsize:
            ret += 1
    return ret


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.63ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.5MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (0.07ms, 10.3MB)
테스트 12 〉	통과 (0.36ms, 10.3MB)
테스트 13 〉	통과 (0.30ms, 10.3MB)
테스트 14 〉	통과 (1.14ms, 10.1MB)
테스트 15 〉	통과 (1.39ms, 10.4MB)
테스트 16 〉	통과 (0.14ms, 10.3MB)
테스트 17 〉	통과 (0.27ms, 10.3MB)
테스트 18 〉	통과 (0.68ms, 10.4MB)
테스트 19 〉	통과 (1.24ms, 10.4MB)
테스트 20 〉	통과 (0.83ms, 10.3MB)
테스트 21 〉	통과 (1.51ms, 10.4MB)
테스트 22 〉	통과 (1.12ms, 10.1MB)
테스트 23 〉	통과 (1.74ms, 10.4MB)
테스트 24 〉	통과 (3.58ms, 10.4MB)
테스트 25 〉	통과 (1.83ms, 10.6MB)
테스트 26 〉	통과 (1.68ms, 10.5MB)
테스트 27 〉	통과 (1.92ms, 10.4MB)
테스트 28 〉	통과 (1.98ms, 10.5MB)
테스트 29 〉	통과 (1.91ms, 10.5MB)
테스트 30 〉	통과 (1.96ms, 10.5MB)
테스트 31 〉	통과 (0.44ms, 10.4MB)
테스트 32 〉	통과 (0.95ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''