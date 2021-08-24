크레인 인형뽑기

def solution(board, moves):
    answer = 0
    moved = []
    for x in moves:
        x -= 1
        for i in range(len(board)):
            if board[i][x] != 0:
                moved.append(board[i][x])
                board[i][x] = 0
                if moved[-1] == moved[-2]:
                    moved.pop(-1)
                    moved.pop(-1)
                    answer += 2
    return answer