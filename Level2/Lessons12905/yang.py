# 가장 큰 정사각형 찾기
def solution(board):
    import copy
    y = len(board)
    x = len(board[0])
    arr = copy.deepcopy(board)
    for i in range(y):
        for j in range(x):
            if i == 0 or j == 0:
                arr[i][j] = board[i][j]
            else:
                arr[i][j] = 0
    arr[0] = board[0]
    for i in range(1,y):
        arr[i][0] = board[i][0]
    
    for i in range(1, y):
        for j in range(1, x):
            if board[i][j] == 1:
                arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1

    answer = 0
    for i in range(y):
        tmp = max(arr[i])
        answer = max(answer, tmp)
    
    return answer**2
# 테스트 1 〉	통과 (1.22ms, 10.3MB)
# 테스트 2 〉	통과 (1.22ms, 10.4MB)
# 테스트 3 〉	통과 (1.28ms, 10.3MB)
# 테스트 4 〉	통과 (1.26ms, 10.3MB)
# 테스트 5 〉	통과 (1.29ms, 10.2MB)
# 테스트 6 〉	통과 (1.19ms, 10.3MB)
# 테스트 7 〉	통과 (1.32ms, 10.3MB)
# 테스트 8 〉	통과 (3.30ms, 10.3MB)
# 테스트 9 〉	통과 (1.15ms, 10.2MB)
# 테스트 10 〉	통과 (1.32ms, 10.3MB)
# 테스트 11 〉	통과 (1.21ms, 10.4MB)
# 테스트 12 〉	통과 (1.33ms, 10.4MB)
# 테스트 13 〉	통과 (1.25ms, 10.3MB)
# 테스트 14 〉	통과 (1.31ms, 10.4MB)
# 테스트 15 〉	통과 (1.25ms, 10.3MB)
# 테스트 16 〉	통과 (1.29ms, 10.4MB)
# 테스트 17 〉	통과 (1.27ms, 10.3MB)
# 테스트 18 〉	통과 (3.64ms, 10.4MB)
# 테스트 19 〉	통과 (2.80ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (827.60ms, 40.3MB)
# 테스트 2 〉	통과 (792.13ms, 39.5MB)
# 테스트 3 〉	통과 (835.47ms, 39.8MB)