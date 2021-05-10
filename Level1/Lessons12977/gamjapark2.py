# 소수 만들기 - 에라토스테네스의 체

import itertools
def prime(n):
    arr = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i+i, n, i):
                arr[j] = False

    return [i for i in range(2, n) if arr[i]]

def solution(nums):
    answer = 0
    n = [sum(x) for x in list(itertools.combinations(nums,3))]
    n.sort()
    p = prime(n[-1] + 1)
    for i in n:
        if i in p:
            answer += 1
    return answer

'''
테스트 1 〉	통과 (2.17ms, 10.4MB)
테스트 2 〉	통과 (2.52ms, 10.2MB)
테스트 3 〉	통과 (0.74ms, 10.3MB)
테스트 4 〉	통과 (2.44ms, 10.3MB)
테스트 5 〉	통과 (3.19ms, 10.4MB)
테스트 6 〉	통과 (11.73ms, 10.6MB)
테스트 7 〉	통과 (1.04ms, 10.3MB)
테스트 8 〉	통과 (26.17ms, 11.4MB)
테스트 9 〉	통과 (2.79ms, 10.3MB)
테스트 10 〉	통과 (27.32ms, 11.4MB)
테스트 11 〉	통과 (0.10ms, 10.3MB)
테스트 12 〉	통과 (0.07ms, 10.2MB)
테스트 13 〉	통과 (0.15ms, 10.3MB)
테스트 14 〉	통과 (0.07ms, 10.3MB)
테스트 15 〉	통과 (0.43ms, 10.2MB)
테스트 16 〉	통과 (67.73ms, 11.5MB)
테스트 17 〉	통과 (90.95ms, 12.3MB)
테스트 18 〉	통과 (1.18ms, 10.3MB)
테스트 19 〉	통과 (0.59ms, 10.3MB)
테스트 20 〉	통과 (87.08ms, 12.3MB)
테스트 21 〉	통과 (79.05ms, 12.1MB)
테스트 22 〉	통과 (16.60ms, 10.7MB)
테스트 23 〉	통과 (0.03ms, 10.3MB)
테스트 24 〉	통과 (66.53ms, 11.7MB)
테스트 25 〉	통과 (66.98ms, 11.6MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
'''