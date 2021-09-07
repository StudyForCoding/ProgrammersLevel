# 최솟값 만들기

```python
def solution(A,B):
    lst = []
    
    for i in range(len(A)):
        lst.append(min(A)*max(B))
        A.remove(min(A))
        B.remove(max(B))   
    return sum(lst)

# 첫 번째 행렬의 min값 * 두 번째 행렬의 max값, 값들 remove => 최솟값 아닐까?
##효율성테스트 시간초과나서 실패
```

```python
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    lst = []
    for i in range(len(A)):
        lst.append(A[i]*B[i])  
    return sum(lst)

# 첫 번째 행렬의 min값 * 두 번째 행렬의 max값, 값들 remove => 최솟값 아닐까?
```

