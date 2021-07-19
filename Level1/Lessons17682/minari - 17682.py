# 다트게임

```python
import re

def solution(dartResult):
    answer = 0    
    power = {'S':1, 'D':2, 'T':3}
    mul = {'':1, '*':2, '#':-1}
    
    rep = re.compile('(\d+)([SDT])([*#]?)')
    score = rep.findall(dartResult)
    
    for i in range(len(score)):
        if score[i][2] == '*' and i>0:
            score[i-1] *= 2
        score[i] = int(score[i][0])**power[score[i][1]]*mul[score[i][2]]
        
    answer = sum(score)
    return answer

#1. S = 점수**1 , D = 점수**2, T = 점수**3
#2. * = 해당 점수*2 + 직전 점수*2 , 첫번째에서 나올 시 해당점수*2 , 중첩될 시 *4
#3. # = 해당 점수 -
#4. 와 # 중첩가능, 해당 점수*-2
```

