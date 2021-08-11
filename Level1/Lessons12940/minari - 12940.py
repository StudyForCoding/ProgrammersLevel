# 최대공약수와 최소공배수

```python
def solution(n, m):
    from math import gcd
    answer = [gcd(n,m),int(n*m/gcd(n,m))]
    return answer
```

