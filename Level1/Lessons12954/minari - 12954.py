# x만큼 간격이 있는 n개의 숫자

```python
def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer

# x부터 시작
# x씩 증가하는 숫자를 n개만큼 리스트에 출력

```

```python
def solution(x, n):
    return [x*i for i in range(1,n+1)]

# x부터 시작
# x씩 증가하는 숫자를 n개만큼 리스트에 출력
```

