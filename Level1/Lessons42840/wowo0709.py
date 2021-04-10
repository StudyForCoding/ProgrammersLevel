def solution(answers):
    p1 = [1,2,3,4,5]           # 학생1의 패턴
    p2 = [2,1,2,3,2,4,2,5]     # 학생2의 패턴
    p3 = [3,3,1,1,2,2,4,4,5,5] # 학생3의 패턴
    N,M,K = len(p1),len(p2),len(p3)
    correct = [0,0,0]          # 각 학생이 맞힌 개수
    for i in range(len(answers)):
        if p1[i%N] == answers[i]: correct[0] += 1
        if p2[i%M] == answers[i]: correct[1] += 1
        if p3[i%K] == answers[i]: correct[2] += 1
    max_correct = max(correct)
    answer = []
    answer = [i+1 for i in range(3) if correct[i] == max_correct]
    return answer