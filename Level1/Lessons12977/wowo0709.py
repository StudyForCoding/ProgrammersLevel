# 소수 만들기

from math import sqrt

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(i+1,j):
                flag = 1
                num = nums[i] + nums[k] + nums[j]
                for n in range(2,int(sqrt(num))+1):
                    if num % n == 0:
                        flag = 0
                        break
                if flag: answer += 1

    return answer

'''
테스트 1 〉	통과 (3.45ms, 10.2MB)
테스트 2 〉	통과 (4.57ms, 10.2MB)
테스트 3 〉	통과 (0.88ms, 10.2MB)
테스트 4 〉	통과 (0.74ms, 10.2MB)
테스트 5 〉	통과 (3.00ms, 10.3MB)
테스트 6 〉	통과 (4.09ms, 10.3MB)
테스트 7 〉	통과 (0.26ms, 10.1MB)
테스트 8 〉	통과 (10.36ms, 10.2MB)
테스트 9 〉	통과 (1.19ms, 10.3MB)
테스트 10 〉	통과 (9.91ms, 10.3MB)
테스트 11 〉	통과 (0.12ms, 10.1MB)
테스트 12 〉	통과 (0.07ms, 10.2MB)
테스트 13 〉	통과 (0.16ms, 10.2MB)
테스트 14 〉	통과 (0.06ms, 10.3MB)
테스트 15 〉	통과 (0.06ms, 10.1MB)
테스트 16 〉	통과 (11.10ms, 10.2MB)
테스트 17 〉	통과 (9.69ms, 10.3MB)
테스트 18 〉	통과 (0.14ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (15.05ms, 10.3MB)
테스트 21 〉	통과 (14.49ms, 10.2MB)
테스트 22 〉	통과 (2.29ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (11.77ms, 10.2MB)
테스트 25 〉	통과 (11.82ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
'''