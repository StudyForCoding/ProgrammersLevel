# 소수 만들기

import itertools
def isPrime(n):
    if n == 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def solution(nums):
    return sum([isPrime(sum(x)) for x in list(itertools.combinations(nums,3))])

'''
테스트 1 〉	통과 (2.67ms, 10.3MB)
테스트 2 〉	통과 (3.93ms, 10.4MB)
테스트 3 〉	통과 (1.04ms, 10.3MB)
테스트 4 〉	통과 (0.89ms, 10.3MB)
테스트 5 〉	통과 (4.46ms, 10.3MB)
테스트 6 〉	통과 (6.19ms, 10.6MB)
테스트 7 〉	통과 (0.37ms, 10.3MB)
테스트 8 〉	통과 (12.28ms, 10.9MB)
테스트 9 〉	통과 (1.40ms, 10.3MB)
테스트 10 〉	통과 (11.27ms, 11.1MB)
테스트 11 〉	통과 (0.18ms, 10.3MB)
테스트 12 〉	통과 (0.09ms, 10.2MB)
테스트 13 〉	통과 (0.25ms, 10.2MB)
테스트 14 〉	통과 (0.10ms, 10.1MB)
테스트 15 〉	통과 (0.09ms, 10.3MB)
테스트 16 〉	통과 (13.24ms, 11.1MB)
테스트 17 〉	통과 (12.39ms, 11.5MB)
테스트 18 〉	통과 (0.18ms, 10.3MB)
테스트 19 〉	통과 (0.02ms, 10.3MB)
테스트 20 〉	통과 (18.89ms, 11.7MB)
테스트 21 〉	통과 (16.05ms, 11.7MB)
테스트 22 〉	통과 (2.51ms, 10.4MB)
테스트 23 〉	통과 (0.02ms, 10.1MB)
테스트 24 〉	통과 (17.17ms, 11MB)
테스트 25 〉	통과 (14.89ms, 11.1MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
'''