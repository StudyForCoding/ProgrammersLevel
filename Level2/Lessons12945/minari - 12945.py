 # 피보나치 수

```python
import sys
def solution(n):
    def fibo(n):
        if n <= 2:
            return 1
        else:
            return fibo(n-1)%1234567 + fibo(n-2)%1234567
    
    sys.setrecursionlimit(10**7)
    return fibo(n) % 1234567

## 7번부터 시간초과로 실패
```

```python
def solution(n):
    answer = 0
    fibo=[0]*(n+1)
    fibo[1]=1
    for i in range(2,n+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
    return fibo[n]%1234567
```

