# [1차] 프렌즈4블록
def solution(m, n, board):
    newboard = [[board[j][i] for j in range(m)][::-1] for i in range(n)]
    while True: 
        popList = set()
        for i in range(1,n):
            for j in range(1,m):
                try:
                    if newboard[i][j] == newboard[i-1][j] == newboard[i][j-1] == newboard[i-1][j-1]:
                        popList = popList.union({(i,j),(i-1,j),(i,j-1),(i-1,j-1)})
                except:
                    continue
        
        popList = sorted(list(popList),key=lambda x:x[1],reverse=True)
        if popList:
            for i,j in popList: del newboard[i][j]
        else:
            return m*n - sum(list(map(len,newboard)))

'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (4.62ms, 10.3MB)
테스트 5 〉	통과 (29.60ms, 10.4MB)
테스트 6 〉	통과 (3.81ms, 10.2MB)
테스트 7 〉	통과 (1.95ms, 10.3MB)
테스트 8 〉	통과 (4.69ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.86ms, 10.3MB)
테스트 11 〉	통과 (4.88ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''