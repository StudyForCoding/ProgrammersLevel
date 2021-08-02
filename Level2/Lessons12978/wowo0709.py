# 배달
def find_shortest_path(startV, graph):
    # dijkstra algorithm
    from heapq import heappush, heappop
    weights = [float('inf') for _ in range(len(graph)+1)]
    weights[startV] = 0
    heap = []
    heappush(heap, (weights[startV], startV)) # (가중치, 노드) 전달 (정렬 기준: 가중치)
    while heap:
        cw, cv = heappop(heap)
        # 현재 노드까지의 다른 경로 중 더 작은 가중치를 가지는 경로가 있으면 pass. 
        if weights[cv] < cw: continue 
        for nw, nv in graph[cv]:
            if cw + nw < weights[nv]:
                weights[nv] = cw + nw
                heappush(heap,(weights[nv],nv))

    return weights # 최단경로 리스트 반환

def solution(N, road, K):
    graph = {i+1:[] for i in range(N)}
    for u,v,w in road: 
        graph[u].append((w,v))
        graph[v].append((w,u))
    shortest_path = find_shortest_path(1,graph)
    return sum([True for w in shortest_path if w <= K])

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (0.08ms, 10.4MB)
테스트 13 〉	통과 (0.07ms, 10.3MB)
테스트 14 〉	통과 (0.85ms, 10.5MB)
테스트 15 〉	통과 (1.13ms, 10.5MB)
테스트 16 〉	통과 (0.05ms, 10.3MB)
테스트 17 〉	통과 (0.06ms, 10.4MB)
테스트 18 〉	통과 (0.37ms, 10.3MB)
테스트 19 〉	통과 (1.06ms, 10.5MB)
테스트 20 〉	통과 (0.28ms, 10.3MB)
테스트 21 〉	통과 (1.25ms, 10.5MB)
테스트 22 〉	통과 (0.42ms, 10.3MB)
테스트 23 〉	통과 (1.31ms, 10.6MB)
테스트 24 〉	통과 (0.91ms, 10.5MB)
테스트 25 〉	통과 (1.81ms, 10.5MB)
테스트 26 〉	통과 (1.70ms, 10.8MB)
테스트 27 〉	통과 (1.77ms, 10.8MB)
테스트 28 〉	통과 (1.68ms, 10.7MB)
테스트 29 〉	통과 (1.74ms, 10.7MB)
테스트 30 〉	통과 (1.63ms, 10.8MB)
테스트 31 〉	통과 (0.09ms, 10.3MB)
테스트 32 〉	통과 (0.12ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''