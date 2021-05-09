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