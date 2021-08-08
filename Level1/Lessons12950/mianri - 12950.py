# 행렬의 덧셈

```python
def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] + arr2[i][j] == answer[i][j]    
    return answer
```

- IndexError: list index out of range

```python
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]   
    return arr1


#for문, 2차원배열의 열개수로
#arr1[i][j] + arr2[i][j] = answer[i][j]
```

