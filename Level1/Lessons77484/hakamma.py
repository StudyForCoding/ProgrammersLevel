#77484 로또의 최고순위와 최저순위

def solution(lottos, win_nums):
    answer = []
    min_rank = 7
    count = 0
    
    for i in lottos:
        if i in win_nums:
            min_rank -= 1
        elif i == 0:
            count += 1
    
    if min_rank - count == 7:
        min_rank -= 1
    
    answer.append(min_rank - count)
    
    if min_rank == 7:
        min_rank -= 1
    
    answer.append(min_rank)
    
    return answer