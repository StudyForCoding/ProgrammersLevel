# 소수 찾기

```python
def solution(n):
    prime_number = set(range(2,n+1))
    for i in range(2,n+1):
        if i in prime_number:
            prime_number -= set(range(i*2,n+1,i))
    return len(prime_number)
    
```

