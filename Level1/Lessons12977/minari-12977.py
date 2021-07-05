def Prime(plus_num):
    if plus_num > 1:
        for i in range(2,plus_num):
            if plus_num % i == 0:
                return False
    else:
        return False
    return True

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                plus_num = nums[i] + nums[j] + nums[k]
                if Prime(plus_num) == True:
                    answer +=1
    return answer

#1. nums 중 3개 뽑음
#2. plus_num = 뽑은 3개를 더함
#3. 2부터 plus_num 까지 for문 돌려서, 모든 n이 plus_num % n != 0 이라면 answer += 1