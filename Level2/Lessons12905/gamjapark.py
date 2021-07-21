# 가장 큰 정사각형 찾기

def solution(board):
    answer = 0
    row = len(board)
    if row == 1:
        answer = max(board[0])

    col = len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j]:
                board[i][j] += min(board[i-1][j-1], board[i][j-1], board[i-1][j])
                if answer < board[i][j]:
                    answer = board[i][j]
    answer **=2
    return answer


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.06ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (0.05ms, 10.3MB)
테스트 16 〉	통과 (0.07ms, 10.3MB)
테스트 17 〉	통과 (0.06ms, 10.2MB)
테스트 18 〉	통과 (1.42ms, 10.2MB)
테스트 19 〉	통과 (2.13ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (421.33ms, 31.1MB)
테스트 2 〉	통과 (400.73ms, 30.7MB)
테스트 3 〉	통과 (431.73ms, 30.8MB)
채점 결과
정확성: 59.6
효율성: 40.4
합계: 100.0 / 100.0
'''