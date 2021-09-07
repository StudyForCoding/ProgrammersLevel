# N개의 최소공배수

```python
from math import gcd

def lcm(x,y):
    return x*y//gcd(x,y)

def solution(arr):
    while True:
        arr.append(lcm(arr.pop(0),arr.pop(0)))
        if len(arr) == 1:
            return arr[0]
            
        
#arr = n개의 숫자 배열, 숫자들 모두의 최소공배수 반환

```

