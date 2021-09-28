# 올바른 괄호

```python
def solution(s):
    answer = True
    sum = 0
    for i in range(len(s)):
        if s[i] == "(":
            sum += 1
        elif s[i] == ")":
            sum -= 1
        #)부터 시작하는 경우 False
        if sum < 0:
            return False
        
    if sum == 0:
        return True
    else:
        return False

# '('들어오면 +1, ')'들어오면 -1 해서 sum = 0 이면 True, sum != 0 이면 False
```

