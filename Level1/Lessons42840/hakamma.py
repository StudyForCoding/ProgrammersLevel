def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            scores[0] += 1
        
        if answers[i] == b[i%len(b)]:
            scores[1] += 1
        
        if answers[i] == c[i%len(c)]:
            scores[2] += 1
            
    result = max(scores)
    
    for k in range(len(scores)):
        if scores[k] == result:
            answer.append(k+1)

    return answer