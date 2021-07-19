```python
def solution(nums):
    answer = 0
    num = []
    
    #1.
    for i in range(len(nums)):
        if nums[i] not in num:
            num.append(nums[i])

    #2.
    if len(num) <= (len(nums)/2):
        return len(num)
    elif len(num) > (len(nums)/2):
        return len(nums)/2


#1. nums 에서 종류가 다른 번호들 모으기
#2. 종류가 다른 번호들 모은 수의 최대 : N/2
```

