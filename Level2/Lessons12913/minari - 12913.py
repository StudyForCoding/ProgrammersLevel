# 땅따먹기

```python
def solution(land):
    answer = 0
    for i in range(len(land)-1):
        add = max(land[i])
        index = land[i].index(max(land[i]))
        land[i].pop(index)
        add_2 = max(land[i])
        for j in range(4):
            if j == index:
                land[i+1][j] += add_2
            else:
                land[i+1][j] += add
    return max(land[-1])
```

