#42889 ½ÇÆÐÀ²

def solution(N, stages):
    answer = []
    total = len(stages)
    rate = {}
    
    for i in range(1,N+1):
        if total != 0 :
            fail = stages.count(i)
            rate[i] = fail/total
            total -= fail
        else:
            rate[i] = 0
    answer = sorted(rate, key=lambda x: rate[x], reverse=True)
    
    return answer