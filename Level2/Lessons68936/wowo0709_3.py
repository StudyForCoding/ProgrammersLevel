# 쿼드 압축 후 개수 세기

# 제일 간결한 코드
# 참조: https://hynnjnn.tistory.com/25
def solution(arr):
    h = len(arr) // 2
    if sum([sum(i) for i in arr]) == len(arr)**2:
        return [0, 1]
    elif sum([sum(i) for i in arr]) == 0:
        return [1, 0]
    else:
        return [sum(i) for i in zip(*[solution([i[:h] for i in arr[:h]]),
                                      solution([i[h:] for i in arr[:h]]),
                                      solution([i[:h] for i in arr[h:]]),
                                      solution([i[h:] for i in arr[h:]])])]

'''
정확성  테스트
테스트 1 〉	통과 (1.30ms, 10.3MB)
테스트 2 〉	통과 (1.63ms, 10.2MB)
테스트 3 〉	통과 (0.54ms, 10.2MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (533.79ms, 12.6MB)
테스트 6 〉	통과 (127.51ms, 12.6MB)
테스트 7 〉	통과 (56.70ms, 12.8MB)
테스트 8 〉	통과 (22.03ms, 12.6MB)
테스트 9 〉	통과 (9.47ms, 12.8MB)
테스트 10 〉	통과 (5.46ms, 18.9MB)
테스트 11 〉	통과 (0.08ms, 10.3MB)
테스트 12 〉	통과 (0.14ms, 10.2MB)
테스트 13 〉	통과 (13.62ms, 12.6MB)
테스트 14 〉	통과 (103.48ms, 20.7MB)
테스트 15 〉	통과 (173.59ms, 20.7MB)
테스트 16 〉	통과 (74.00ms, 12.6MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''