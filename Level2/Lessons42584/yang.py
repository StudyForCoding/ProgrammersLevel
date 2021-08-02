# 주식가격
def solution(prices):
    answer = [0] * len(prices)
    for idx1 in range(len(prices)):
        for idx2 in range(idx1 + 1, len(prices)):
            if prices[idx1] > prices[idx2]:
                answer[idx1] += 1
                break
            else:
                answer[idx1] += 1
    
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (1.13ms, 10.2MB)
# 테스트 4 〉	통과 (1.18ms, 10.3MB)
# 테스트 5 〉	통과 (1.51ms, 10.3MB)
# 테스트 6 〉	통과 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (0.75ms, 10.2MB)
# 테스트 8 〉	통과 (0.88ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.2MB)
# 테스트 10 〉	통과 (1.50ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (154.87ms, 18.9MB)
# 테스트 2 〉	통과 (121.27ms, 17.6MB)
# 테스트 3 〉	통과 (181.54ms, 19.5MB)
# 테스트 4 〉	통과 (139.06ms, 18.2MB)
# 테스트 5 〉	통과 (87.12ms, 16.9MB)