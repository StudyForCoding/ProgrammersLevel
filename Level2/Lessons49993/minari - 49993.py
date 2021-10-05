# 스킬트리

```python
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_lst = list(skill)
        
        for i in skills:
            if i in skill:
                if i != skill_lst.pop(0):
                    break
        else:
            answer += 1
    return answer
```

