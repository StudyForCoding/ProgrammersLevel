# 쿼드압축 후 개수 세기

def quadtree(arr):

    l = len(arr)
    if l == 1: return [1,0] if arr[0][0] == 0 else [0,1]

    lu = quadtree([a[:l//2] for a in arr[:l//2]])
    ru = quadtree([a[l//2:] for a in arr[:l//2]])
    ld = quadtree([a[:l//2] for a in arr[l//2:]])
    rd = quadtree([a[l//2:] for a in arr[l//2:]])

    if lu == ru == ld == rd == [1,0] or \
        lu == ru == ld == rd == [0,1]: return lu
    else: return list(map(sum,zip(lu,ru,ld,rd)))

def solution(arr):
    return quadtree(arr)

'''
정확성  테스트
테스트 1 〉	통과 (1.44ms, 10.3MB)
테스트 2 〉	통과 (1.31ms, 10.3MB)
테스트 3 〉	통과 (1.36ms, 10.3MB)
테스트 4 〉	통과 (0.38ms, 10.3MB)
테스트 5 〉	통과 (265.86ms, 12.6MB)
테스트 6 〉	통과 (238.92ms, 12.6MB)
테스트 7 〉	통과 (233.99ms, 12.7MB)
테스트 8 〉	통과 (230.72ms, 12.8MB)
테스트 9 〉	통과 (209.33ms, 12.6MB)
테스트 10 〉	통과 (950.55ms, 20.7MB)
테스트 11 〉	통과 (0.37ms, 10.3MB)
테스트 12 〉	통과 (0.35ms, 10.2MB)
테스트 13 〉	통과 (206.64ms, 12.7MB)
테스트 14 〉	통과 (891.77ms, 20.7MB)
테스트 15 〉	통과 (894.10ms, 20.8MB)
테스트 16 〉	통과 (239.40ms, 12.6MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''