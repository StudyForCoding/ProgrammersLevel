```python
def solution(N, stages):
    answer = []
    total = len(stages)
    failure_rate = [0 for _ in range(N)]
    
    #2.
    for i in range(1,N+1):
        fail = stages.count(i)
        if total == 0:
            failure_rate[i-1] = 0
        else:
            failure_rate[i-1] = (fail / total)
        total -= fail

    #3.
    sort_failure = sorted(failure_rate,reverse=True)
    
    for k in range(len(failure_rate)):
        answer.append(failure_rate.index(sort_failure[k])+1)    #내림차순으로 정렬한 실패율의 첫번째 요소부터 인덱스 번호 저장하기(인덱스는 0부터 시작하므로 +1의 번호 저장)
        failure_rate[failure_rate.index(sort_failure[k])]=2     #failure_rate의 최댓값이 1이므로, 탐색한 failure_rate의 요소를 2로 바꾸어서 중복 탐색 방지하기
    return answer

#1. 실패율 = 스테이지에 도달했지만 클리어x / 스테이지에 도달,클리어
#2. 스테이지마다 실패율 계산 -> 리스트에 담기
#3. 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 넣기 -> return
```

