# 하샤드 수

```python
def solution(x):
    x = str(x)
    plus = 0
    #1.
    for i in range(len(x)):
        plus += int(x[i])
    
    #2,3
    if int(x) % plus == 0:
        return True
    else:
        return False

#1. plus += str x의 자릿수
#2. int(x) % plus == 0
#3. == 하샤드 수
```

