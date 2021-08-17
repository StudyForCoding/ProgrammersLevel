#주식가격
def solution(prices):
    time = len(prices)
    answer = [0 for i in range(time)]
    for idx,price in enumerate(prices):
        for i in range(idx+1,time):
            if prices[i] >= price:
                answer[idx] += 1
            else:
                answer[idx] += 1
                break
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (0.98ms, 10.3MB)
테스트 4 〉	통과 (1.17ms, 10.3MB)
테스트 5 〉	통과 (1.28ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.72ms, 10.3MB)
테스트 8 〉	통과 (0.78ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
테스트 10 〉	통과 (1.41ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (137.73ms, 18.8MB)
테스트 2 〉	통과 (107.64ms, 17.6MB)
테스트 3 〉	통과 (159.77ms, 19.6MB)
테스트 4 〉	통과 (115.75ms, 18.3MB)
테스트 5 〉	통과 (76.29ms, 17.1MB)
'''