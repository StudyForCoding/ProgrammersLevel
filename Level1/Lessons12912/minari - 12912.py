# 두 정수 사이의 합

```python
def solution(a, b):
    answer = 0
    if a<b:
        for i in range(a,b+1):
            answer += i
    else:
        for i in range(b,a+1):
            answer += i
    return answer
```

```python
def solution(a, b):
    if a<b:
        return sum(range(a,b+1))
        
    else:
        return sum(range(b,a+1))
```

