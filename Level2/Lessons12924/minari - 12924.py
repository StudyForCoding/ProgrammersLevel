# 숫자의 표현

```python
def solution(n):
    answer = 0
    for i in range(1,(n//2)+1):
        add = 0
        for j in range(i,n+1):
            add += j
            if add == n:
                answer += 1
                break
            elif add > n:
                break
    return answer + 1 # 자기자신

```

