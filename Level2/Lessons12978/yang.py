# 배달
import sys
INF = sys.maxsize
def alg(n, arr):
    
    dist = [[INF] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = arr[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
def solution(N, road, K):
    tmp_arr1 = sorted(road, key = lambda x : x[0])
    tmp_arr2 = sorted(road, key = lambda x : x[1])
    n = max(tmp_arr1[-1][0], tmp_arr2[-1][1])
    
    arr = [[INF]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if x == y:
                arr[y][x] = 0
    for way in road:
        arr[way[0]-1][way[1]-1] = min(way[2], arr[way[0]-1][way[1]-1])
        arr[way[1]-1][way[0]-1] = min(way[2], arr[way[1]-1][way[0]-1])

    dist = alg(n,arr)
    answer = 0
    for num in dist[0]:
        if num <= K:
            answer += 1
    return answer
# 테스트 1 〉	통과 (0.14ms, 10.3MB)
# 테스트 2 〉	통과 (0.06ms, 10.3MB)
# 테스트 3 〉	통과 (0.08ms, 10.4MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.34ms, 10.3MB)
# 테스트 6 〉	통과 (0.10ms, 10.3MB)
# 테스트 7 〉	통과 (0.10ms, 10.3MB)
# 테스트 8 〉	통과 (0.11ms, 10.3MB)
# 테스트 9 〉	통과 (0.04ms, 10.3MB)
# 테스트 10 〉	통과 (0.27ms, 10.3MB)
# 테스트 11 〉	통과 (0.34ms, 10.3MB)
# 테스트 12 〉	통과 (9.82ms, 10.4MB)
# 테스트 13 〉	통과 (5.79ms, 10.3MB)
# 테스트 14 〉	통과 (5.70ms, 10.3MB)
# 테스트 15 〉	통과 (10.11ms, 10.4MB)
# 테스트 16 〉	통과 (1.74ms, 10.3MB)
# 테스트 17 〉	통과 (4.44ms, 10.3MB)
# 테스트 18 〉	통과 (18.57ms, 10.4MB)
# 테스트 19 〉	통과 (18.23ms, 10.5MB)
# 테스트 20 〉	통과 (16.73ms, 10.3MB)
# 테스트 21 〉	통과 (14.57ms, 10.5MB)
# 테스트 22 〉	통과 (19.39ms, 10.4MB)
# 테스트 23 〉	통과 (22.68ms, 10.5MB)
# 테스트 24 〉	통과 (16.06ms, 10.5MB)
# 테스트 25 〉	통과 (22.41ms, 10.7MB)
# 테스트 26 〉	통과 (21.42ms, 10.6MB)
# 테스트 27 〉	통과 (16.83ms, 10.6MB)
# 테스트 28 〉	통과 (22.54ms, 10.7MB)
# 테스트 29 〉	통과 (22.60ms, 10.6MB)
# 테스트 30 〉	통과 (21.77ms, 10.6MB)
# 테스트 31 〉	통과 (20.49ms, 10.4MB)
# 테스트 32 〉	통과 (20.49ms, 10.3MB)