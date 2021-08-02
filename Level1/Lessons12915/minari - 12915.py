# 문자열 내 마음대로 정렬하기

```python
def solution(strings, n):
    return sorted(sorted(strings), key=lambda str : str[n])

#strings의 n번째 인덱스를 기준으로 sorted
```

