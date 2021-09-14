# 다음 큰 숫자

```python
def solution(n):
    binary = format(n, 'b')
    count = binary.count('1')
    while True:
        n += 1
        if count == format(n, 'b').count('1'):
            return n
```

