```python
def solution(d, budget):
    answer = 0
    
    d.sort()    #1.
    
    #2.
    for i in range(len(d)):
        if budget - d[i] >= 0:
            answer += 1
            budget = budget - d[i]            
        else:
            break
    
    return answer


#1. 최대한 많은 부서의 물품지원 -> 지원금액이 작은 부서부터 채워야 많은 부서를 지원 가능
#2. 부서가 지원한 금액 그대로를 주어야함. ( 모자라게 줄 수 없음 ) -> for문 돌려서 d[i] 값을 budget에서 빼기
```

