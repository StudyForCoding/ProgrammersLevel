#순위 검색
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(myval)]

    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.21ms, 10.5MB)
테스트 2 〉	통과 (0.22ms, 10.4MB)
테스트 3 〉	통과 (0.42ms, 10.5MB)
테스트 4 〉	통과 (2.69ms, 10.5MB)
테스트 5 〉	통과 (2.38ms, 10.6MB)
테스트 6 〉	통과 (4.51ms, 10.6MB)
테스트 7 〉	통과 (6.33ms, 10.8MB)
테스트 8 〉	통과 (38.96ms, 11.5MB)
테스트 9 〉	통과 (41.89ms, 13.3MB)
테스트 10 〉	통과 (41.50ms, 13.9MB)
테스트 11 〉	통과 (2.32ms, 10.6MB)
테스트 12 〉	통과 (4.66ms, 10.8MB)
테스트 13 〉	통과 (3.37ms, 10.8MB)
테스트 14 〉	통과 (20.88ms, 12.1MB)
테스트 15 〉	통과 (20.88ms, 12.2MB)
테스트 16 〉	통과 (2.32ms, 10.6MB)
테스트 17 〉	통과 (4.72ms, 10.8MB)
테스트 18 〉	통과 (20.88ms, 12.2MB)
효율성  테스트
테스트 1 〉	통과 (732.93ms, 64.2MB)
테스트 2 〉	통과 (664.68ms, 64.5MB)
테스트 3 〉	통과 (720.85ms, 63.8MB)
테스트 4 〉	통과 (662.25ms, 64.2MB)
'''