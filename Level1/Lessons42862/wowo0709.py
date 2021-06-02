def solution(n, lost, reserve):
    answer = 0
    for i in range(1,n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    for i in range(1,n+1):
        if i not in lost:
            answer += 1
        if i in lost:
            for offset in [-1,0,1]:
                if i+offset in reserve:
                    reserve.remove(i+offset)
                    answer += 1
                    break
    return answer