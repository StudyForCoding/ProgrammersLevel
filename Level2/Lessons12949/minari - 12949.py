# 행렬의 곱셈

```python
def solution(arr1, arr2):
    answer = []
    for a in range(len(arr1)):
        lst = []
        a_lst = arr1[a]
        for b in range(len(arr2[0])):
            b_lst = []
            for c in range(len(arr2)):
                b_lst.append(arr2[c][b])
            lst.append(sum([p*q for p, q in zip(a_lst, b_lst)]))
        answer.append(lst)
    return answer


# 행끼리 열끼리 곱한 결과 출력
# 행렬의 곱셈 : 첫 번째 행렬의 열의 길이, 두 번째 행렬의 행의 길이 따름
#             a11*b11 + a12*b21 + a13*b31 + ... = c11
#             a11*b12 + a12*b22 + a13*b32 + ... = c12

```

