# 방문 길이

```python
def solution(dirs):
    answer = 0
    length = [[0 for _ in range(11)] for _ in range(11)] 
    x,y = 5,5 # -5~5까지가 아니라 0~10로 했으니까 시작지점은 5,5
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            y += 1
            length[x][y] += 1
        if dirs[i] == 'D':
            y -= 1
            length[x][y] += 1
        if dirs[i] == 'R':
            x += 1
            length[x][y] += 1
        if dirs[i] == 'L':
            x -= 1
            length[x][y] += 1
            
```

```python
def solution(dirs):
    x,y = 0,0
    length = set() #중복 없는 집합 설정하기

    # 좌표이동 저장한 for문
    for i in dirs:
        if i == 'U' and y < 5:
            length.add(((x,y),(x,y+1)))
            y += 1
        elif i == 'D' and y > -5:
            length.add(((x,y-1),(x,y)))
            y -= 1
        elif i == 'R' and x < 5:
            length.add(((x,y),(x+1,y)))
            x += 1
        elif i == 'L' and x > -5:
            length.add(((x-1,y),(x,y)))
            x -= 1
        
    return len(length)
```

for i in range(len(dirs)): 로 할거면 dirs[i] == 'U' 로 써줘야하ㅗ

for i in dirs: 로 할거면 i == 'U'로 써줘야하는데 뭔차이일까

```python
def solution(dirs):
    x,y = 0,0
    length = set() #중복 없는 집합 설정하기

    # 좌표이동 저장한 for문
    for i in dirs:
        if i == 'U' and y < 5:
            length.add(((x,y),(x,y+1)))
            y += 1
        elif i == 'D' and y > -5:
            length.add(((x,y),(x,y-1)))
            y -= 1
        elif i == 'R' and x < 5:
            length.add(((x,y),(x+1,y)))
            x += 1
        elif i == 'L' and x > -5:
            length.add(((x,y),(x-1,y)))
            x -= 1
        
    return len(length)
```

이렇게  진행하면 테스트8부터 실패해 왜?

