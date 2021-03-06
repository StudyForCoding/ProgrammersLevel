# 가장 큰 정사각형

def solution(board):

    for i in range(1, len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] >= 1:
                board[i][j] = min(board[i - 1][j],board[i][j - 1],board[i - 1][j - 1]) + 1

    return max([n for arr in board for n in arr])**2

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.07ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.3MB)
테스트 15 〉	통과 (0.06ms, 10.2MB)
테스트 16 〉	통과 (0.07ms, 10.2MB)
테스트 17 〉	통과 (0.10ms, 10.2MB)
테스트 18 〉	통과 (1.26ms, 10.2MB)
테스트 19 〉	통과 (1.26ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (406.99ms, 39.7MB)
테스트 2 〉	통과 (410.46ms, 39MB)
테스트 3 〉	통과 (423.82ms, 39.3MB)
채점 결과
정확성: 59.6
효율성: 40.4
합계: 100.0 / 100.0
'''