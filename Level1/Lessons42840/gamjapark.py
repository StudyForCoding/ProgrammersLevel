def solution(answers):
    dic = {5:[1,2,3,4,5], 8:[2,1,2,3,2,4,2,5], 10:[3,3,1,1,2,2,4,4,5,5] }
    scores = {5:0, 8:0, 10:0}
    for i, a in enumerate(answers):
        for j in [5, 8, 10]:
            if dic[j][i%j] == a:
                scores[j] += 1
    
    values = list(scores.values())
    n = max(values)
    result = []
    for i in range(len(values)):
        if values[i] == n:
            result.append(i+1)
    return result