# 1차 프렌즈4블록
import copy
def pull(board):
    board_copy = copy.deepcopy(board)
    cnt = 0
    for y in range(len(board)):
        for x in reversed(range(len(board[0]))):
            if board[y][x] == '9':
                cnt += 1
                del board[y][x]
        for _ in range(cnt):
            board[y].append('9')

        cnt = 0
    return board
            
def cal(board):
    tmp = []
    flag = False
    for y in range(len(board)-1):
        for x in range(len(board[0])-1):
            if board[y][x] == board[y+1][x] == board[y][x+1] == board[y+1][x+1] and board[y][x] != '9':
                tmp.append([y,x])
                flag = True
    for pair in tmp:
        board[pair[0]][pair[1]] = '9'
        board[pair[0] + 1][pair[1]] = '9'
        board[pair[0]][pair[1] + 1] = '9'
        board[pair[0] + 1][pair[1] + 1] = '9'
    return board, flag
def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    for i in range(len(board)):
        board[i] = board[i][::-1]
    while(1):
        board, flag = cal(board)

        if flag == False:
            break
        board = pull(board)

        
    answer = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == '9':
                answer += 1
    return answer
# 테스트 1 〉	통과 (0.09ms, 10.3MB)
# 테스트 2 〉	통과 (0.12ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (1.61ms, 10.4MB)
# 테스트 5 〉	통과 (141.24ms, 10.3MB)
# 테스트 6 〉	통과 (10.45ms, 10.3MB)
# 테스트 7 〉	통과 (0.95ms, 10.3MB)
# 테스트 8 〉	통과 (1.81ms, 10.3MB)
# 테스트 9 〉	통과 (0.09ms, 10.4MB)
# 테스트 10 〉	통과 (1.21ms, 10.3MB)
# 테스트 11 〉	통과 (5.00ms, 10.3MB)