# [3차] 파일명 정렬

import re

def solution(files):
    answer = []
    for i in range(len(files)):
        name = re.split('(\d+)',files[i]) # 숫자 문자 split
        name.append(name[0].lower())
        name.append(int(name[1][:5]))
        answer.append(name)
    answer.sort(key=lambda x: (x[-2],x[-1]))
    answer = list(map(lambda x: "".join(x[:len(x)-2]), answer))
    return answer

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.16ms, 10.4MB)
테스트 2 〉	통과 (0.15ms, 10.3MB)
테스트 3 〉	통과 (2.56ms, 10.9MB)
테스트 4 〉	통과 (3.39ms, 10.8MB)
테스트 5 〉	통과 (2.93ms, 10.7MB)
테스트 6 〉	통과 (3.11ms, 10.7MB)
테스트 7 〉	통과 (2.95ms, 10.7MB)
테스트 8 〉	통과 (2.39ms, 10.6MB)
테스트 9 〉	통과 (2.85ms, 10.8MB)
테스트 10 〉	통과 (2.95ms, 10.8MB)
테스트 11 〉	통과 (2.64ms, 10.7MB)
테스트 12 〉	통과 (3.37ms, 11MB)
테스트 13 〉	통과 (2.61ms, 11MB)
테스트 14 〉	통과 (3.47ms, 11.2MB)
테스트 15 〉	통과 (3.47ms, 11.2MB)
테스트 16 〉	통과 (3.07ms, 10.9MB)
테스트 17 〉	통과 (2.53ms, 10.9MB)
테스트 18 〉	통과 (2.60ms, 10.7MB)
테스트 19 〉	통과 (2.83ms, 10.7MB)
테스트 20 〉	통과 (3.15ms, 10.9MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''