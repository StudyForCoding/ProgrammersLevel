# 다트게임
def solution(dartResult):
    answer = []
    result = []
    for x in dartResult:
        dartResult = dartResult.replace("10",'A')
    dartResult = list(dartResult)
    for x in dartResult:
        result.append(x.replace('A','10'))
    print(result)

    for idx in range(1, len(result)):
        if result[idx] == 'S':
            answer.append(int(result[idx - 1]))
        elif result[idx] == 'D':
            answer.append(int(result[idx - 1]) ** 2)
        elif result[idx] == 'T':
            answer.append(int(result[idx - 1]) ** 3)
        
        if result[idx] ==  '*':
            answer[-1] = answer[-1] * 2
            if len(answer) >= 2:
                answer[-2] = answer[-2] * 2
        elif result[idx] == '#':
            answer[-1] = answer[-1] * -1
    answer = sum(answer)
    return answer
# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.4MB)
# 테스트 5 〉	통과 (0.04ms, 10.3MB)
# 테스트 6 〉	통과 (0.04ms, 10.5MB)
# 테스트 7 〉	통과 (0.04ms, 10.4MB)
# 테스트 8 〉	통과 (0.03ms, 10.4MB)
# 테스트 9 〉	통과 (0.04ms, 10.5MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.03ms, 10.3MB)
# 테스트 13 〉	통과 (0.04ms, 10.4MB)
# 테스트 14 〉	통과 (0.04ms, 10.3MB)
# 테스트 15 〉	통과 (0.04ms, 10.4MB)
# 테스트 16 〉	통과 (0.08ms, 10.4MB)
# 테스트 17 〉	통과 (0.03ms, 10.4MB)
# 테스트 18 〉	통과 (0.04ms, 10.3MB)
# 테스트 19 〉	통과 (0.04ms, 10.4MB)
# 테스트 20 〉	통과 (0.04ms, 10.5MB)
# 테스트 21 〉	통과 (0.04ms, 10.3MB)
# 테스트 22 〉	통과 (0.06ms, 10.4MB)
# 테스트 23 〉	통과 (0.04ms, 10.3MB)
# 테스트 24 〉	통과 (0.04ms, 10.4MB)
# 테스트 25 〉	통과 (0.04ms, 10.3MB)
# 테스트 26 〉	통과 (0.03ms, 10.5MB)
# 테스트 27 〉	통과 (0.03ms, 10.3MB)
# 테스트 28 〉	통과 (0.04ms, 10.4MB)
# 테스트 29 〉	통과 (0.04ms, 10.5MB)
# 테스트 30 〉	통과 (0.04ms, 10.4MB)
# 테스트 31 〉	통과 (0.04ms, 10.3MB)
# 테스트 32 〉	통과 (0.03ms, 10.5MB)