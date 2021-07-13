```python
def solution(lottos, win_nums):
    answer = []
    rank = 0
    # lottos 리스트와 win_nums 리스트를 비교해서 맞은 개수 구함
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                rank += 1
    answer.append(rank) 
    
    # worst 수에 0 개수만큼 더함
    for i in range(len(lottos)):
        if lottos[i] == 0:
            rank +=1
    answer.append(rank)
    
    # 맞은 개수와 순위 일치시키기
    for i in range(len(answer)):
        if answer[i] == 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] ==  4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else:
            answer[i] = 6
    
    # 최고 순위를 리스트 앞에 위치시키기위해 순서 뒤집음
    answer.reverse()
    
    return answer


#1. 민우의 로또번호와 win_nums가 몇 개 맞는지 확인
#2. worst = lottos와 win_nums 맞은 개수 , best = 맞은 개수 + 0의 개수 
#3. 맞은 개수와 순위 일치시키기
```

