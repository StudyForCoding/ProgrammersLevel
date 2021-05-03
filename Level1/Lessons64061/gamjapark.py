def solution(board, moves):
    answer = 0
    b = []
    for x in zip(*board):
        item = []
        for i in x:
            if i != 0:
                item.append(i)
        item.reverse()
        b.append(item)

    result = []
    for m in moves:
        if len(b[m-1]) != 0:
            a = b[m-1].pop()
            if not result:
                result.append(a)
                continue
            t = result.pop()
            if a == t:
                answer += 2
            else:
                result.append(t)
                result.append(a)
    return answer