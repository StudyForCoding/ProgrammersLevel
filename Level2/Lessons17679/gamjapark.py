# [1차]프렌츠4블록
import numpy as np

def new_borad(m, n, board):
    remove =  np.array([[True for _ in range(m)] for _ in range(n)])
    count = 0
    for i in range(n - 1):
        for j in range(m - 1):
            cur = board[i,j]
            if cur == "-1":
                break
            if cur == board[i,j+1] and cur == board[i+1,j] and cur == board[i+1,j+1]:
                remove[i,j] = False
                remove[i,j+1] = False
                remove[i+1,j] = False
                remove[i+1,j+1] = False
                count += 1
    new_map = []
    remove_count = 0
    for i in range(n):
        tmp = board[i][remove[i]].tolist()
        while len(tmp) < m:
            tmp.append("-1")
            remove_count += 1
        new_map.append(tmp)
    return new_map, count, remove_count
    
def solution(m, n, board):
    answer = 0
    b = np.array(list(map(lambda x:list(x), board)))
    b_t = np.transpose(b)
    new_b = b_t[...,::-1]
    count = -1
    while count != 0:
        new_b, count, remove_count = new_borad(m, n, new_b)
        answer += remove_count
        new_b = np.array(new_b)
    return answer


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.13ms, 27.9MB)
테스트 2 〉	통과 (0.19ms, 27.8MB)
테스트 3 〉	통과 (0.26ms, 27.7MB)
테스트 4 〉	통과 (1.92ms, 28MB)
테스트 5 〉	통과 (103.88ms, 28MB)
테스트 6 〉	통과 (8.26ms, 28MB)
테스트 7 〉	통과 (1.22ms, 27.6MB)
테스트 8 〉	통과 (2.04ms, 27.7MB)
테스트 9 〉	통과 (0.15ms, 27.6MB)
테스트 10 〉	통과 (0.99ms, 27.6MB)
테스트 11 〉	통과 (2.55ms, 28MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
