#1845 ÆùÄÏ¸ó

def solution(nums):
    answer = 0
    nums.sort()
    length = len(nums) // 2
    value = 0
    
    for k in nums:
        if(k != value and answer < length):
            answer += 1
            value = k
    return answer