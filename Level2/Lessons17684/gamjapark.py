# [3차]압축

import string

def solution(msg):
    words = string.ascii_uppercase
    words_dict = {words[i]:i+1 for i in range(26)}
    
    msg_len = len(msg)
    if msg_len == 1:
        return [words_dict[msg[0]]]
    answer = []
    add_idx = 27
    start, end = 0, 1
    
    while end <= msg_len:
        w = msg[start:end]
        if end == msg_len:
            answer.append(words_dict[w])
            break
        c = msg[end]
        try:
            tmp = words_dict[w+c]
            end += 1
        except:
            answer.append(words_dict[w])
            words_dict[w+c] = add_idx
            add_idx += 1
            start = end
            end = start + 1
    return answer


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.20ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.37ms, 10.3MB)
테스트 7 〉	통과 (0.29ms, 10.3MB)
테스트 8 〉	통과 (0.34ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.4MB)
테스트 10 〉	통과 (0.33ms, 10.3MB)
테스트 11 〉	통과 (0.22ms, 10.3MB)
테스트 12 〉	통과 (0.40ms, 10.3MB)
테스트 13 〉	통과 (0.45ms, 10.3MB)
테스트 14 〉	통과 (0.47ms, 10.3MB)
테스트 15 〉	통과 (0.54ms, 10.4MB)
테스트 16 〉	통과 (0.37ms, 10.3MB)
테스트 17 〉	통과 (0.30ms, 10.3MB)
테스트 18 〉	통과 (0.12ms, 10.3MB)
테스트 19 〉	통과 (0.15ms, 10.3MB)
테스트 20 〉	통과 (0.35ms, 10.4MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''

