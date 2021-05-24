# [1차] 다트 게임 - re 미사용

def solution(dartResult):
    len_str = len(dartResult)
    default_region = {'S':1, 'D':2, 'T':3}
    score = []
    region = []
    option1 = [0 for _ in range(3)] # option list for *
    option2 = [1 for _ in range(3)] # option list for #
    start = i = j = 0
    while i < len_str:
        try:
            region.append(default_region[dartResult[i]])
            score.append(int(dartResult[start:i]))
            if i + 1 != len_str and not dartResult[i + 1].isnumeric():
                if dartResult[i + 1] == '#':
                    option2[j] = -1
                else:
                    if j-1 >= 0:
                        option1[j-1] += 1
                    option1[j] += 1
                start = i + 2     # S*10T
                i += 3 
            else:
                start = i + 1
                i += 2
            j += 1
        except:
            i += 1
    return sum([(score[i]**region[i]) * (2**option1[i]) * option2[i] for i in range(3)])

'''

테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.5MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.5MB)
테스트 5 〉	통과 (0.04ms, 10.6MB)
테스트 6 〉	통과 (0.04ms, 10.5MB)
테스트 7 〉	통과 (0.04ms, 10.5MB)
테스트 8 〉	통과 (0.04ms, 10.5MB)
테스트 9 〉	통과 (0.04ms, 10.5MB)
테스트 10 〉	통과 (0.05ms, 10.4MB)
테스트 11 〉	통과 (0.04ms, 10.5MB)
테스트 12 〉	통과 (0.04ms, 10.5MB)
테스트 13 〉	통과 (0.04ms, 10.5MB)
테스트 14 〉	통과 (0.04ms, 10.5MB)
테스트 15 〉	통과 (0.04ms, 10.5MB)
테스트 16 〉	통과 (0.98ms, 10.4MB)
테스트 17 〉	통과 (0.04ms, 10.6MB)
테스트 18 〉	통과 (0.04ms, 10.5MB)
테스트 19 〉	통과 (0.04ms, 10.5MB)
테스트 20 〉	통과 (0.04ms, 10.4MB)
테스트 21 〉	통과 (0.04ms, 10.5MB)
테스트 22 〉	통과 (0.04ms, 10.4MB)
테스트 23 〉	통과 (0.04ms, 10.5MB)
테스트 24 〉	통과 (0.04ms, 10.5MB)
테스트 25 〉	통과 (0.08ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.5MB)
테스트 27 〉	통과 (0.04ms, 10.4MB)
테스트 28 〉	통과 (0.04ms, 10.5MB)
테스트 29 〉	통과 (0.05ms, 10.5MB)
테스트 30 〉	통과 (0.04ms, 10.5MB)
테스트 31 〉	통과 (0.05ms, 10.3MB)
테스트 32 〉	통과 (0.04ms, 10.5MB)
'''