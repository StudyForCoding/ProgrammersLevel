from itertools import cycle
def solution(answers):
    answer_supo1 = [1,2,3,4,5]
    answer_supo2 = [2,1,2,3,2,4,2,5]
    answer_supo3 = [3,3,1,1,2,2,4,4,5,5]
    score_supos = [0,0,0]   # supo들이 몇개 맞췄는지 기록
    winner = [] # 이긴사람 저장할 리스트
    # answer_supo리스트들 안의 요소와 answer 값이 맞다면,맞은 개수만큼 score_supos에 저장
    for supo1,supo2,supo3,answer in zip(cycle(answer_supo1),cycle(answer_supo2),cycle(answer_supo3),answers):
            if answer == supo1:
                score_supos[0] += 1 
            if answer == supo2:
                score_supos[1] += 1
            if answer == supo3:
                score_supos[2] += 1 
    # score_supos중 가장 큰 값을 가진 요소를 winner 리스트에 저장                 
    for i in range(len(score_supos)):
        if score_supos[i] == max(score_supos):
            winner.append(i+1)
    return winner