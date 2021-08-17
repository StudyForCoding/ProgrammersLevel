#[1차] 프렌즈4블록
def solution(m, n, board):
    answer = 0
    score = 0
    post = ['' for j in range(m)]
    mark = [[0 for i in range(n)] for j in range(m)]
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != ' ':
                mark[i][j] = mark[i][j+1] = mark[i+1][j] = mark[i+1][j+1] = 1

    for i in range(m):
        score += sum(mark[i])

    if score == 0:
        return 0

    for i in reversed(range(m)):
        for j in range(n):
            if mark[i][j] == 0:
                post[i] += board[i][j]
            else:
                k = i-1
                while(k>=0):
                    if mark[k][j] == 0:
                        post[i] += board[k][j]
                        mark[k][j] = 1
                        break
                    k -= 1
                if len(post[i]) < j+1:
                    post[i] += ' '
    
    return score+solution(m, n, post)

'''
테스트 1 〉	통과 (0.08ms, 10.2MB)
테스트 2 〉	통과 (0.09ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (2.26ms, 10.3MB)
테스트 5 〉	통과 (87.78ms, 13.1MB)
테스트 6 〉	통과 (9.80ms, 10.2MB)
테스트 7 〉	통과 (1.47ms, 10.3MB)
테스트 8 〉	통과 (2.56ms, 10.3MB)
테스트 9 〉	통과 (0.06ms, 10.3MB)
테스트 10 〉	통과 (1.36ms, 10.2MB)
테스트 11 〉	통과 (5.42ms, 10.3MB)
'''