# 땅따먹기
def solution(land):
    idxes = [0,1,2,3]
    for i in range(1, len(land)):
        land_sort = sorted(land[i-1])
        max_idx = land[i-1].index(land_sort[-1])
        for idx in idxes:
            if max_idx == idx:
                land[i][idx] += land_sort[-2]
            else:
                land[i][idx] += land_sort[-1]
    return max(land[-1])


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (1.67ms, 10.2MB)
테스트 2 〉	통과 (0.92ms, 10.5MB)
테스트 3 〉	통과 (1.18ms, 10.4MB)
테스트 4 〉	통과 (0.87ms, 10.4MB)
테스트 5 〉	통과 (0.90ms, 10.4MB)
테스트 6 〉	통과 (1.23ms, 10.4MB)
테스트 7 〉	통과 (1.30ms, 10.4MB)
테스트 8 〉	통과 (1.25ms, 10.4MB)
테스트 9 〉	통과 (0.85ms, 10.3MB)
테스트 10 〉	통과 (0.99ms, 10.4MB)
테스트 11 〉	통과 (0.87ms, 10.4MB)
테스트 12 〉	통과 (2.85ms, 10.4MB)
테스트 13 〉	통과 (1.39ms, 10.4MB)
테스트 14 〉	통과 (1.16ms, 10.4MB)
테스트 15 〉	통과 (1.29ms, 10.4MB)
테스트 16 〉	통과 (1.31ms, 10.2MB)
테스트 17 〉	통과 (1.30ms, 10.2MB)
테스트 18 〉	통과 (1.14ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (91.00ms, 32.4MB)
테스트 2 〉	통과 (90.69ms, 32.5MB)
테스트 3 〉	통과 (85.69ms, 32.4MB)
테스트 4 〉	통과 (86.88ms, 32.4MB)
채점 결과
정확성: 59.8
효율성: 40.2
합계: 100.0 / 100.0
'''