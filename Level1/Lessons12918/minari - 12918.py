# 문자열 다루기 기본

```python
def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False
    
# if len(s) == 4 or 6 이라고만 하면 왜 자꾸 길이조건이 안될까
```

