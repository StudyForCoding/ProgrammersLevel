# [1차] 다트게임

def solution(dartResult):
    scores,score = [],''
    N = len(dartResult)
    for i in range(N):
        if dartResult[i].isdigit(): 
            score += dartResult[i]
            op_start = i+1
        elif i+1 == N or dartResult[i+1].isdigit(): 
            op_end = i
            scores = getScore(scores,int(score),dartResult[op_start:op_end+1])
            score = ''
    return sum(scores)
        
def getScore(scores,score,ops):
    for op in ops:
        if op == 'S': continue
        elif op == 'D': score **= 2
        elif op == 'T': score **= 3
        elif op == '*':
            score *= 2
            if scores: scores[-1] *= 2
        elif op == '#':
            score *= -1 
    scores.append(score)
    return scores

'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.5MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.4MB)
테스트 16 〉	통과 (0.03ms, 10.4MB)
테스트 17 〉	통과 (0.03ms, 10.4MB)
테스트 18 〉	통과 (0.03ms, 10.4MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.03ms, 10.4MB)
테스트 21 〉	통과 (0.03ms, 10.3MB)
테스트 22 〉	통과 (0.03ms, 10.2MB)
테스트 23 〉	통과 (0.03ms, 10.4MB)
테스트 24 〉	통과 (0.04ms, 10.4MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (0.03ms, 10.4MB)
테스트 27 〉	통과 (0.04ms, 10.4MB)
테스트 28 〉	통과 (0.04ms, 10.4MB)
테스트 29 〉	통과 (0.03ms, 10.4MB)
테스트 30 〉	통과 (0.03ms, 10.4MB)
테스트 31 〉	통과 (0.03ms, 10.5MB)
테스트 32 〉	통과 (0.04ms, 10.4MB)
'''