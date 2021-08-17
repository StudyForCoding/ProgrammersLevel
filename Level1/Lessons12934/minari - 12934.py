# 정수 제곱근 판별

```python
def solution(n):
    x = n**(1/2)
    if x == int(x):
        return (x+1)**2
    else:
        return -1
    
# x = n**(1/2) , x == int(x)라면 return(x+1)**2
# x != int(x)라면 return -1
```

