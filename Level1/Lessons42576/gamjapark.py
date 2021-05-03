def solution(participant, completion):
    answer=""
    dic = dict()
    for p in participant:
        try:    dic[p] += 1
        except: dic[p] = 1

    for c in completion:
        dic[c] -= 1
        
    for p in participant:
        if dic[p]:
            answer = p
            break
    return answer