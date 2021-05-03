완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for c in range(len(completion)):
        for p in range(len(participant)):
            if participant[p] == completion[c]:
                participant.remove(participant[p])
                break
    return (participant[len(participant)-1])