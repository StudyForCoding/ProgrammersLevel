# 자연수 뒤집어 배열로 만들기

``` python
def solution(n):
    answer = [int(i) for i in str(n)]
    return answer[::-1]
```

