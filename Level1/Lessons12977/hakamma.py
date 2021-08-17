#12977

def solution(nums):
    answer = 0
    result_sum = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                result_sum = nums[i] + nums[j] + nums[k]
                
                for t in range(2, result_sum):
                    if result_sum % t == 0:
                        break
                    
                else:
                    answer += 1
    
    return answer