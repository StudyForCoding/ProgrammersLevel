# 쿼드압축 후 개수 세기

# 배열의 인덱스 값을 매개변수로 전달함으로써 시간 단축
def quadtree(x, y, l, arr):
    
    if l == 1: return [1, 0] if arr[x][y] == 0 else [0, 1]
    
    lu = quadtree(x, y, l//2, arr)
    ru = quadtree(x, y+l//2, l//2, arr)
    ld = quadtree(x+l//2, y, l//2, arr)
    rd = quadtree(x+l//2, y+l//2, l//2, arr)
    
    if lu == ru == ld == rd == [1,0] or \
        lu == ru == ld == rd == [0,1]: return lu
    else: return list(map(sum,zip(lu,ru,ld,rd)))

def solution(arr):
    return quadtree(0, 0, len(arr), arr)
        
'''
정확성  테스트
테스트 1 〉	통과 (0.78ms, 10.2MB)
테스트 2 〉	통과 (0.82ms, 10.2MB)
테스트 3 〉	통과 (0.62ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (128.97ms, 12.2MB)
테스트 6 〉	통과 (96.16ms, 12.1MB)
테스트 7 〉	통과 (81.70ms, 12.2MB)
테스트 8 〉	통과 (77.82ms, 12.2MB)
테스트 9 〉	통과 (86.34ms, 12.1MB)
테스트 10 〉	통과 (379.43ms, 18.9MB)
테스트 11 〉	통과 (0.15ms, 10.3MB)
테스트 12 〉	통과 (0.14ms, 10.2MB)
테스트 13 〉	통과 (79.36ms, 12.2MB)
테스트 14 〉	통과 (317.70ms, 18.9MB)
테스트 15 〉	통과 (321.03ms, 18.9MB)
테스트 16 〉	통과 (84.79ms, 12.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''