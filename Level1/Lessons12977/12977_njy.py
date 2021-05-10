# 소수 만들기

def solution(nums):
    length = len(nums)
    total = []
    answer = 0

    # 3중 for문으로 모든 조합 구하기
    for a in range(length):
        for b in range(a+1,length):
            for c in range(b+1,length):
                divisor = 2
                count = 0
                sum = nums[a]+nums[b]+nums[c]
                # while문으로 2부터 n-1까지 modulation
                while(divisor < sum):
                    if sum%divisor == 0:
                        break
                    else:
                        divisor += 1
                        count += 1
                # 나머지가 모두 0이 아니면 answer += 1
                if count == sum-2:
                    answer += 1

    return answer

"""
테스트 1 〉	통과 (4.22ms, 10.3MB)
테스트 2 〉	통과 (5.29ms, 10.2MB)
테스트 3 〉	통과 (1.82ms, 10.3MB)
테스트 4 〉	통과 (1.25ms, 10MB)
테스트 5 〉	통과 (6.12ms, 10.2MB)
테스트 6 〉	통과 (38.91ms, 10.2MB)
테스트 7 〉	통과 (1.41ms, 10.2MB)
테스트 8 〉	통과 (78.95ms, 10.2MB)
테스트 9 〉	통과 (21.55ms, 10.2MB)
테스트 10 〉    통과 (164.76ms, 10.1MB)
테스트 11 〉    통과 (0.31ms, 10.1MB)
테스트 12 〉    통과 (0.13ms, 10.2MB)
테스트 13 〉    통과 (0.30ms, 10.3MB)
테스트 14 〉    통과 (0.13ms, 10.3MB)
테스트 15 〉    통과 (0.10ms, 10.2MB)
테스트 16 〉    통과 (268.18ms, 10.2MB)
테스트 17 〉    통과 (4.59ms, 10.3MB)
테스트 18 〉    통과 (3.86ms, 10.2MB)
테스트 19 〉    통과 (0.56ms, 10.2MB)
테스트 20 〉    통과 (363.66ms, 10.1MB)
테스트 21 〉    통과 (317.99ms, 10.2MB)
테스트 22 〉    통과 (1.26ms, 10.2MB)
테스트 23 〉    통과 (0.01ms, 10.3MB)
테스트 24 〉    통과 (272.63ms, 10.1MB)
테스트 25 〉    통과 (281.43ms, 10.2MB)
테스트 26 〉    통과 (0.01ms, 10.1MB)
"""