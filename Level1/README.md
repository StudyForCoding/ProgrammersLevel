# Level1
프로그래머스 Level1 문제 풀이

---

### 문제 목록

- 두 개 뽑아서 더하기 - [Lessons68644](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons68644/README.md)
- 크레인 인형뽑기 게임 - [Lessons64061](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons64061/README.md)
- 완주하지 못한 선수 - [Lessons42576](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons42576/README.md)
- 신규 아이디 추천 - [Lessons72410](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons72410/README.md)
- 모의고사 - [Lessons42840](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons42840/README.md)
- K번째수 - [Lessons42748](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons42748/README.md)
- 체육복 - [Lessons42862](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons42862/README.md)
- 2016년 - [Lessons12901](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons12901/README.md)
- 3진법 뒤집기 - [Lessons68935](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons68935/README.md)
- 가운데 글자 가져오기 - [Lessons12903](https://github.com/StudyForCoding/ProgrammersLevel/tree/master/Level1/Lessons12903/README.md)

### 두 개 뽑아서 더하기 - Lessons68644

- 관련 정보
    - 집합 자료형
        - 중복을 허용하지 않는다.
        - 순서가 없다.
- 코드

```python
def solution(numbers):
    answer = []

    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer
```

### 크레인 인형뽑기 게임 - Lessons64061

- 관련 정보
- 코드

```python
def solution(board, moves):
    bucket = []
    answer = 0

    for move in moves:
        for row in range(len(board)):
            if(board[row][move-1]!=0):
                bucket.append(board[row][move-1])
                board[row][move-1] = 0
                if(len(bucket)>1):
                    if(bucket[-1]==bucket[-2]):
                        bucket = bucket[:-2]
                        answer = answer+2
                break
    return answer
```

### 완주하지 못한 선수 - Lessons42576

- 관련 정보
    - remove(x)
    - remove(x) 함수는 리스트에서 값이 x와 같은 첫 번째 요소를 제거합니다.
- 코드
    - 실패

    ```python
    def solution(participant, completions):
        for completion in completions:
            participant.remove(completion)
        return participant[0] 
    ```

    ```python
    def solution(participants, completion):
        for participant in participants:
            if completion.count(participant) != participants.count(participant):
                return participant
    ```

    - 성공

    ```python
    def solution(participants, completions):
        count_c = {}
        count_p = {}

        for participant in participants:
            count_c[participant] = 0
            try: count_p[participant] += 1
            except: count_p[participant] = 1

        for completion in completions:
            try: count_c[completion] += 1
            except: count_c[completion] += 1

        for participant in participants:
            if count_p[participant] != count_c[participant]:
                return participant
    ```

### 신규 아이디 추천 - Lessons72410

- 관련 정보
- 코드

```python
from re import *
def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    new_id = sub('[\~\!\@\#\$\%\^\&\*\(\)\=\+\[\{\]\}\:\?\,\<\>\/]', '', new_id)

    new_id = sub('[.]{2,1000}','.',new_id)

    if new_id[0] == '.' and len(new_id) > 0:
        while new_id[0] == '.' :
            new_id = new_id.replace('.',"",1)
            if new_id == '':
                break

    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id.rstrip('.')

    if new_id == "":
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')

    if len(new_id) <= 2:
        while True:
            new_id = new_id + new_id[-1]
            if len(new_id) >= 3:
                break

    answer = new_id
    return answer
```

### 모의고사 - Lessons42840

- 관련 정보
- 코드

```python
def solution(answers):
    pattern1 = [1,3,4,5]
    flag1 = 0
    supo=[0,0,0]

    for idx,answer in enumerate(answers):
        a1 = idx%5 + 1
        if (answer == a1):
            supo[0] += 1

        if idx%2 == 0:
            a2 = 2
        else:
            a2 = pattern1[flag1%4]
            flag1 += 1

        if answer == a2:
            supo[1] += 1

        a3 = idx%10
        if(a3 < 2):
            a3 = 3
        elif a3 < 4:
            a3 = 1
        elif a3 < 6:
            a3 = 2
        elif a3 < 8:
            a3 = 4
        elif a3 < 10:
            a3 = 5

        if answer == a3:
            supo[2] += 1

    best = 0
    answer = [0]

    for idx,score in enumerate(supo):

        if score>best:
            best = score
            answer = [0]
            answer[0] = idx+1

        elif score==best:
            answer.append(idx+1)
    
    return answer
```

### K번째수 - Lessons42748

- 관련 정보
- 코드

```python
def solution(array, commands):
    answer = []
    for command in commands:
        temp = array
        temp = temp[command[0]-1:command[1]]
        temp.sort()
        answer.append(temp[command[2]-1])
    return answer
```

### 체육복 - Lessons42862

- 관련 정보
- 코드

```python
def solution(n, losts, reserves):
    answer = []
    for i in range(n):
        answer.append(1)

    for reserve in reserves:
        answer[reserve-1] += 1

    for lost in losts:
        answer[lost-1] -= 1

    for i in range(n):
        if answer[i] == 0:
            if i == 0:
                if answer[1] == 2:
                    answer[0],answer[1] = 1,1
            elif i == n-1:
                if answer[n-2] == 2:
                    answer[n-1],answer[n-2] = 1,1
            elif answer[i-1] == 2:
                answer[i],answer[i-1] = 1,1
            elif answer[i+1] == 2:
                answer[i],answer[i+1] = 1,1

    return answer.count(1)+answer.count(2)
```

### 2016년 - Lessons12901

- 관련 정보
- 코드

```python
def solution(a, b):
    answer = ''
    day=["SUN","MON","TUE","WED","THU","FRI","SAT"]
    last=[31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    
    return day[(sum(last[:a-1]) + b + 4) % 7]
```

### 3진법 뒤집기 - Lessons689350

- 관련 정보
- 코드

```python
def solution(n):
    ter=""
    answer=0
    while True:
        ter=str(n%3)+ter
        n=n//3
        if n==0:
            break
            
    for exp in range(len(ter)):
        answer=answer+(3**exp*int(ter[exp]))
    return answer
```

### 가운데 글자 가져오기 - Lessons12903

- 관련 정보
    - round to the nearest; ties to even
        - round to the nearest는 우리가 아닌 일반적인 반올림 방식과 같지만 ties to even에서 차이가 생긴다.
        - 여기서 말하는 tie는기준 값을 중심으로 절반 예를 들면, 1.5는 1과 2와의 차이가 딱 절반이다.
        - 이 때, 계산하는 방식이 다르다.
        - ties to even을 해석하면, 짝수를 만들기 위해 앞자리 수가 홀수면 올림, 짝수면 내림을 취한다.
        - 그래서 round( 1.5 )와 round( 2.5 )의 결과가 2로 같게 된다.
- 코드
- 실패

```python
def solution(s):
    answer = ''
    if len(s)%2 == 1:
        answer = s[round(len(s)/2)]
    else:
        answer = s[round(len(s)/2)-1:int(len(s)/2)+1]
    return answer
```

- 성공

```python
def solution(s):
    answer = ''
    if len(s)%2 == 1:
        answer = s[int(len(s)/2)]
    else:
        answer = s[int(len(s)/2)-1:int(len(s)/2)+1]
    return answer
```