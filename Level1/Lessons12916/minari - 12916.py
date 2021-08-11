# 문자열 내 p와 y의 개수

```python
def solution(s):
    len_p = 0
    len_y = 0
    for i in range(len(s)):
        if s[i] in ['P','p']:
            len_p += 1
        elif s[i] in ['Y','y']:
            len_y += 1
    if len_p == len_y:
        return True
    elif len_p != len_y:
        return False
```

