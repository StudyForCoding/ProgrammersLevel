# [1차] 다트 게임 - re 사용

import re
def solution(dartResult):
    score = []
    option1 = [0 for _ in range(3)] # option list for *
    option2 = [1 for _ in range(3)] # option list for #
    i = 0
    print(re.split("S|D|T", dartResult))
    for tmp in re.split("S|D|T", dartResult):
        if tmp == '':
            break
        if tmp.isnumeric():
            score.append(int(tmp))
        else:
            if len(tmp) >= 2:
                score.append(int(tmp[1:]))
                
            if tmp[0] == '#':
                option2[i-1] = -1
            else:
                if i-2 >= 0:
                    option1[i-2] += 1
                option1[i-1] += 1
        i += 1
    region = [1 if i == 'S' else 2 if i == 'D' else 3 for i in re.findall("S|D|T", dartResult)]
    return sum([(score[i]**region[i]) * (2**option1[i]) * option2[i] for i in range(3)])

'''
테스트 1 〉	통과 (0.16ms, 10.5MB)
테스트 2 〉	통과 (0.74ms, 10.4MB)
테스트 3 〉	통과 (0.15ms, 10.5MB)
테스트 4 〉	통과 (0.15ms, 10.4MB)
테스트 5 〉	통과 (0.13ms, 10.5MB)
테스트 6 〉	통과 (0.76ms, 10.4MB)
테스트 7 〉	통과 (0.15ms, 10.5MB)
테스트 8 〉	통과 (0.14ms, 10.5MB)
테스트 9 〉	통과 (0.10ms, 10.5MB)
테스트 10 〉	통과 (0.15ms, 10.6MB)
테스트 11 〉	통과 (0.14ms, 10.5MB)
테스트 12 〉	통과 (0.14ms, 10.5MB)
테스트 13 〉	통과 (0.15ms, 10.5MB)
테스트 14 〉	통과 (0.14ms, 10.5MB)
테스트 15 〉	통과 (1.28ms, 10.5MB)
테스트 16 〉	통과 (0.14ms, 10.5MB)
테스트 17 〉	통과 (0.15ms, 10.5MB)
테스트 18 〉	통과 (0.15ms, 10.5MB)
테스트 19 〉	통과 (0.16ms, 10.4MB)
테스트 20 〉	통과 (0.14ms, 10.5MB)
테스트 21 〉	통과 (0.15ms, 10.5MB)
테스트 22 〉	통과 (0.14ms, 10.5MB)
테스트 23 〉	통과 (0.15ms, 10.6MB)
테스트 24 〉	통과 (1.36ms, 10.4MB)
테스트 25 〉	통과 (0.15ms, 10.2MB)
테스트 26 〉	통과 (0.15ms, 10.5MB)
테스트 27 〉	통과 (0.14ms, 10.6MB)
테스트 28 〉	통과 (0.15ms, 10.5MB)
테스트 29 〉	통과 (0.15ms, 10.5MB)
테스트 30 〉	통과 (0.15ms, 10.5MB)
테스트 31 〉	통과 (0.15ms, 10.5MB)
테스트 32 〉	통과 (1.37ms, 10.4MB)
'''