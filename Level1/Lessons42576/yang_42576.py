def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append("127423617263")
    for name in zip(participant, completion):
        if name[0] != name[1]:
            answer = name[0]
            break
    return answer