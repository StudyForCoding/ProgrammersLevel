def solution(board,moves):
    answer = 0
    s = [0]
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                doll = board[i][move-1]
                if doll == s[-1]:
                    s.pop()
                    answer += 2
                else:
                    s.append(doll)
                board[i][move-1] = 0
                break
    return answer