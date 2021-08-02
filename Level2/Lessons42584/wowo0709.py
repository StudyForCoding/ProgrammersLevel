# 주식 가격
def solution(prices):
    answer = []
    N = len(prices)
    for i in range(N):
        for j in range(i,N):
            if prices[i] > prices[j] or j == N-1:
                answer.append(j-i)
                break

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (1.09ms, 10.3MB)
테스트 4 〉	통과 (1.27ms, 10.2MB)
테스트 5 〉	통과 (1.34ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.74ms, 10.3MB)
테스트 8 〉	통과 (0.87ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (1.45ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (143.31ms, 18.7MB)
테스트 2 〉	통과 (104.14ms, 17.6MB)
테스트 3 〉	통과 (175.77ms, 19.6MB)
테스트 4 〉	통과 (127.17ms, 18.3MB)
테스트 5 〉	통과 (85.77ms, 17.1MB)
채점 결과
정확성: 66.7
효율성: 33.3
합계: 100.0 / 100.0
'''