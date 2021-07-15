def solution(absolutes, signs):
    answer = 0    
    for i in range(len(absolutes)):
        if signs[i] is True:      
            answer += int(absolutes[i])
        else:
            answer -= int(absolutes[i])
    return answer


#1. for문 (len(absolutes)), if signs[i] is true: answer += absolutes[i], else: answer -= absolutes[i]
#2. sum(absolutes)