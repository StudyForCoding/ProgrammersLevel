 # 콜라츠 추측

```python
def solution(num):
    answer = 0
    while num>1:
        #1-1
        if num%2 == 0:
            answer += 1
            num = num/2
        #1-2
        else:
            answer += 1
            num = (num*3) + 1
        
        if answer >= 500:
            return -1
    
    return answer
```

