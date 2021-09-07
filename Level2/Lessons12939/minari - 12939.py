# 최댓값과 최솟값

```python
def solution(s):
    s = s.replace(" ","")
    return f"{min(s)} {max(s)}"

## 음의 정수에서 -만 출력됨
```

```python
def solution(s):
    result = list(map(int, s.split(' ')))
    min_s = min(result)
    max_s = max(result)
    return f"{min_s} {max_s}"
```

