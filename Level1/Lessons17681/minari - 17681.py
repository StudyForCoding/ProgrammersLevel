```python

def solution(n, arr1, arr2):
    answer = []
    #1. 십진수 -> 이진수로 변환해서 arr1_bi, arr2_bi에 저장하기
    for num1,num2 in zip(arr1,arr2):
        arr_bi = (bin(num1 | num2)[2:])
        if len(arr_bi) < n:
            arr_bi = '0'*(n-len(arr_bi)) + arr_bi
        arr_bi = arr_bi.replace('0',' ')
        arr_bi = arr_bi.replace('1','#')
        answer.append(arr_bi)
    
    return answer

# 두 지도 중 하나만 벽이어도 벽(1) -> or , 모두 공백(0) -> and -> zip으로는 안돼?
# print(bin(십진수)[2:]) = 이진수 이용

```

