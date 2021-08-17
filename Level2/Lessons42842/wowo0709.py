# 카펫
def solution(brown, yellow):
    size = brown + yellow
    for w in range(size,0,-1):
        if size % w == 0 and (w-2)*(size//w-2)==yellow:
            return [w,size//w] # h = size / w

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (55.42ms, 10.1MB)
테스트 4 〉	통과 (0.47ms, 10.2MB)
테스트 5 〉	통과 (1.08ms, 10.1MB)
테스트 6 〉	통과 (18.49ms, 10.2MB)
테스트 7 〉	통과 (70.08ms, 10.2MB)
테스트 8 〉	통과 (55.03ms, 10.1MB)
테스트 9 〉	통과 (64.82ms, 10.1MB)
테스트 10 〉	통과 (76.32ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''