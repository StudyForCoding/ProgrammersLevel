# 가장 큰 정사각형 찾기

```python
def solution(board):
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                if board[i][j] > answer:
                    answer = board[i][j]
    
    return answer**2

# 배열 [1][1] 부터 반복문 사용해서 탐색
# 현재 위치에서 좌,상,좌상 (정사각형) 중 최솟값 +1 을 현재값으로 저장, 배열 끝까지 반복
# 배열 내 최댓값이 정사각형의 한변의 길이
      
```

