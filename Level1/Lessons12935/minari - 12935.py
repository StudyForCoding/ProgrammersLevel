# 제일 작은 수 제거하기

```python
def solution(arr):
    if len(arr) != 1:
        arr.remove(min(arr))   
    elif len(arr) == 1:
        arr.clear()
        arr.append(-1)
    return arr
```

