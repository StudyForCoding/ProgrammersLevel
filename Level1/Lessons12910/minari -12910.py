```python
#나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
         if arr[i]%divisor == 0:
                answer.append(arr[i])
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
        return answer
    else:
        return answer

#for문으로 arr 배열 안에 있는 값을 divisor로 나누기. %div == 0 일 때 return
#if 나누어 떨어지는 arr가 없다면 -1 return
```

