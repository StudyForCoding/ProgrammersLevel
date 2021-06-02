```python
def solution(board,moves):
    basket=[]
    answer=[]
    for move in moves:
        for i in range(len(board)): # range(len(board)) 에 있는 인형갯수만큼 반복
            if board[i][move-1]>0: # board[][] 안에 인형이 존재할 때에만 실행하도록
                basket.append(board[i][move-1])
                board[i][move-1]=0 # board[][] 초기화
                break
            else:
                pass
        if len(basket)>=2 and basket[len(basket)-1]==basket[len(basket)-2]:
            #다음 move로 이동하기 전, basket에 들어있는 인형의 종류 두개가 같은지 확인
            basket.pop(-1)
            basket.pop(-1)
            answer.append(i)
    return len(answer)*2 #사라지는 인형의 갯수는 answer*2
```

