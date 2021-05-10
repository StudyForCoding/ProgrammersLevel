def solution(n, lost, reserve):
    import copy
    answer = 0
    lost.sort()
    reserve.sort()
    reserve_copy = copy.deepcopy(reserve)
    for stud in reserve_copy:
        if stud in lost:
            lost.remove(stud)
            reserve.remove(stud)

    for stud in reserve:
        if stud - 1 in lost:
            lost.remove(stud - 1)
        elif stud + 1 in lost:
            lost.remove(stud + 1)
    answer = n - len(lost)
    return answer