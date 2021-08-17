# 주식가격
def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)]
    tmp = []
    for time in range(len(prices)):
        while tmp and prices[time] < prices[tmp[-1]]:
                t = tmp.pop()
                answer[t] = time - t
        tmp.append(time)
    return answer


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.38ms, 10.3MB)
테스트 4 〉	통과 (0.44ms, 10.3MB)
테스트 5 〉	통과 (0.52ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.25ms, 10.3MB)
테스트 8 〉	통과 (0.32ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.54ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (29.69ms, 19.4MB)
테스트 2 〉	통과 (21.18ms, 17.9MB)
테스트 3 〉	통과 (30.42ms, 20.3MB)
테스트 4 〉	통과 (23.61ms, 18.7MB)
테스트 5 〉	통과 (17.49ms, 17.3MB)
채점 결과
정확성: 66.7
효율성: 33.3
합계: 100.0 / 100.0
'''
